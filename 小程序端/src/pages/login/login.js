// const app =getApp()
Page({
  data: {
    key:'',
  },
  onReady: function () {
    //获得popup组件
    this.popup = this.selectComponent("#popup");
  },
  showPopup() {

  },
  //确认事件
  _success() {
    console.log('你点击了确定');
    this.popup.hidePopup();
  },
  properties: {
    title:{
      type: String,
      value:''
    },
    content:{
      type:String,
      value: ''
    },
    cancelText:{
      type: String,
      value:''
    },
    confirmText:{
      type:String,
      value:''
    }
  },
  showErrorToast: function(e) {
    wx.showModal({
      title: '提示！',
      confirmText: '朕知道了',
      showCancel: false,
      content: e,
      success: function(res) {
        if (res.confirm) {
          console.log('用户点击确定')
        }
      }
    })
  },
  formSubmit: function(e) {
    var that = this;
    if (e.detail.value.number.length == 0) {
      this.showErrorToast('学号或工号不能为空')
    } else if (e.detail.value.phone.length == 0) {
      this.showErrorToast('手机号不能为空')
    } else if (e.detail.value.phone.length != 11) {
      this.showErrorToast('请输入11位手机号码')
    } else if (e.detail.value.password.length == 0) {
      this.showErrorToast('密码不能为空!')
    } else {
      // post提交表单
  
      wx.request({
        url: 'https://gl.honeypot.work/ksglapp/confirm',
        header: {
          "Content-Type": "application/json"
        },
        method: "GET",
        data: {
          // openid: 'qclqclqcl', //这里先写死微信id
          phone: e.detail.value.phone,
          number: e.detail.value.number,
          password: e.detail.value.password,
          items: JSON.stringify([{
            productId: 1,
            productQuantity: 2
          }, {
            productId: 2,
            productQuantity: 2
          }])
        },
        success: function(res){
          console.log(res)

          if (res.statusCode != 200) {
            wx.showToast({ //这里提示失败原因
              title: res.data.message,
              icon: 'loading',
              duration: 1500
            })
          } else {
            wx.showToast({ 
              title: '请等待',
              icon: 'loading',
              duration: 1500,
              success: function () {
                that.setData({
                  key:res.data.key
                })
                console.log(res.data.key); 
                setTimeout(function () {
            
                  that.popup.showPopup()
                },1500)
              }
            })
            wx.showToast({
              title: '申请已提交', //这里成功
              icon: 'success',
              duration: 1000
            })
          }
        },
        fail: function(res) {
          console.log(fail)
          wx.showToast({
            title: '请求失败',
            icon: 'none',
            duration: 1500
          })
        },
      })
    }
  },
})