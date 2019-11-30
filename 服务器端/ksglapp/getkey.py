import random,time
# Create your views here.


def get_key():
    key_ = ""
    for i in range(6):
        key_ += str(random.randint(0,9))
    print('{}'.format('-'*30))
    print('| 秘钥变更： {0: <15} |'.format(key_))
    print('{}'.format('-'*30))
    return key_