
# Create your views here.
#cyy


from pki import accessProtocol, sm2, SRT_G, contractTAC

from django.contrib.auth.decorators import login_required
from django_redis import get_redis_connection

from django.shortcuts import render,redirect
from pki.models import models
from web3 import Web3

from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo
import random
con = get_redis_connection()

R = SRT_G.RadixTree()
userList = UserInfo.objects.all()
for i in userList:
    R.insert(R.root, i.userID, i.pubkeyInfo)
R.print_tree(R.root, '')
# print(userList, type(userList))

ganche_url = "http://127.0.0.1:7545"


web3 = Web3(Web3.HTTPProvider(ganche_url))
# contract = contractTAC.contractInit()
addr = web3.eth.accounts[0]

# addrNum = 5

#缓存测试
def index1(request):

    request.session['name'] = 'hello'

    print (request.session.get('name'))

    return HttpResponse('陈盈盈Hello!')

#登陆
def index(request):
    pass
    return render(request, 'login/index_1.html', locals())

#x新

# def jiami(request):
#     pass
#     return render(request, 'login/jiami.html')
@csrf_exempt
def luyou(request):
    pass
    return render(request, 'login/luyoutable.html')
@csrf_exempt
def modify(request):
    pass
    # return render(request, 'login/test.html', locals())
    return render(request, 'login/test.html')

@csrf_exempt
def denglu(request):
    if request.method == 'POST':
        userID = request.POST.get('username', None)
        userSignature = request.POST.get('password', None)

        pContent = request.POST.get('pContent', None)
        opType = request.POST.get('opType', None)
        sContent = request.POST.get('sContent', None) #signature
        checkSum = request.POST.get('checkSum', None)
        print("pContent: ", pContent, type(pContent))
        accMsg = accessProtocol.accessProtocol(opType=opType, pContent=pContent, sContent=sContent, checkSum=checkSum)
        print("accMsg: ", accMsg)

        checkSumValid = accMsg.checkSumValid()
        # sContentValid = accMsg.sContentValid()
        userPubkey = R.search(R.root, userID)
        print("userID: ", userID)
        print("userpk: ", userPubkey, type(userPubkey))
        # sigValid = False
        if userPubkey != '':
            print("pContent: ", pContent, type(pContent))
            print("userSignature: ", userSignature, type(userSignature))
            print("userPubkey: ", userPubkey, type(userPubkey))

            # sigValid = sm2.Verify(userSignature, pContent, userPubkey, 64)
            # print("sigValid: ", sigValid)
        # if checkSumValid and sigValid:
        if not userPubkey:
            return JsonResponse({'success': '201', 'msg': '登录失败!'})

        if checkSumValid:
            return JsonResponse({'success': '200', 'msg': '登录成功!'})
        else:
            return JsonResponse({'success': '201', 'msg': '登录失败!'})
    else:
        return render(request, 'login/index.html')




@csrf_exempt
def zhuce(request):
    success_log = '注册成功！'
    info_log = 'Wrong!'
    if request.method == "POST":
        userName = request.POST.get('username', None)
        address = request.POST.get('address', None)
        # print(address, type(address))
        address = address.split()[-1]
        address = address.replace('-', '.')
        # print(address, type(address))
        pubkeyInfo = request.POST.get('publickey', None)
        idNumber = request.POST.get('password', None)
        # print(address, type(address))
        pContent = request.POST.get('pContent', None)

        opType = request.POST.get('opType', None)
        sContent = request.POST.get('sContent', None)
        checkSum = request.POST.get('checkSum', None)
        # addrNum = 5
        addrNum = random.randint(0,90)
        addr = web3.eth.accounts[addrNum]
        accMsg = accessProtocol.accessProtocol(opType=opType, pContent=pContent, sContent=sContent, checkSum=checkSum)
        print(accMsg)
        checkSumValid = accMsg.checkSumValid()
        sContentValid = accMsg.sContentValid()

        print(checkSumValid, sContentValid, addr)

        if pContent == '' or not checkSumValid or not sContentValid:

            return HttpResponse(json.dumps(info_log), content_type='application/json')
        else:

            userID = address + '.' + userName + '.' + idNumber
            print(userID)
            reg =UserInfo(userID=userID, address=addr, pubkeyInfo=pubkeyInfo)
            reg.save()

            res = contractTAC.addUser(addr=addr, id=userID, pubkey=pubkeyInfo)
            print(res)

            addrNum += 1
            R.insert(R.root, userID, pubkeyInfo)
            print(R.search(R.root, userID))
            msg = "ID: " + userID
            return HttpResponse(json.dumps(success_log+ "\n" +msg), content_type='application/json')
    else:
        return render(request, 'login/zhuce.html')


@csrf_exempt
@login_required
def cha_user(request):
    if request.method == "POST":

        f_2 = {'status': '查询失败！'}
        f_3 = {'status': '该用户不存在！'}
        try:
            userID = request.POST.get('username')
            userSignature = request.POST.get('password')

            pContent = request.POST.get('pContent', None)
            opType = request.POST.get('opType', None)
            sContent = request.POST.get('sContent', None)
            checkSum = request.POST.get('checkSum', None)
            print("userID: ", userID)
            print("pContent : ", pContent )
            print("opType : ", opType)
            print("sContent : ", sContent)
            print("checkSum : ", checkSum)

            accMsg = accessProtocol.accessProtocol(opType=opType, pContent=pContent, sContent=sContent,
                                                   checkSum=checkSum)



            checkSumValid = accMsg.checkSumValid()

            userPubkey = R.search(R.root, userID)

            print(userPubkey)

            # sigValid = False
            # if userPubkey != '':
            #     sigValid = sm2.Verify(userSignature, pContent, userPubkey, 64)

            # if checkSumValid and sigValid:
            #     searchResult = R.searchPrefix(R.root, pContent)
            #     return HttpResponse(json.dumps(searchResult), content_type='application/json')
            if checkSumValid :
                searchResult = R.searchPrefix(R.root, pContent)
                print("result: ", searchResult, type(searchResult))
                return HttpResponse(json.dumps(searchResult), content_type='application/json')

            return HttpResponse(json.dumps(f_3), content_type='application/json')
        except:
            return HttpResponse(json.dumps(f_2), content_type='application/json')
    else:
        return render(request, 'login/test.html')


@csrf_exempt
@login_required
def del_user(request):
    if request.method == "POST":
        f_1 = {'status': '删除成功！'}
        f_2 = {'status': '删除失败！'}
        f_3 = {'status': '该用户不存在！'}

        userID = request.POST.get('username')
            # userSignature = request.POST.get('password')
        print("userID: ", userID)
        pContent = request.POST.get('pContent', None)
        opType = request.POST.get('opType', None)
        sContent = request.POST.get('sContent', None)
        checkSum = request.POST.get('checkSum', None)

        accMsg = accessProtocol.accessProtocol(opType=opType, pContent=pContent, sContent=sContent,
                                               checkSum=checkSum)

        checkSumValid = accMsg.checkSumValid()

        userAddress = UserInfo.objects.get(userID=userID).address
        userPubkey = R.search(R.root, userID)
        print("userPubkey",userPubkey, "\n", "checkSumValid: ", checkSumValid)
            # sigValid = False
            # if userPubkey != '':
            #     sigValid = sm2.Verify(userSignature, pContent, userPubkey, 64)

            # if checkSumValid and sigValid:
        if checkSumValid :
            resContract = contractTAC.deleteUser(addr=userAddress)
            print("resContract",resContract)

            res = R.deleteID(R.root, userID)
            print("res", res)
            if res:
                resDel = UserInfo.objects.filter(userID=userID).delete()
                print("resDel", resDel)
                return HttpResponse(json.dumps(f_1), content_type='application/json')

        # return HttpResponse(json.dumps(f_3), content_type='application/json')

        return HttpResponse(json.dumps(f_2), content_type='application/json')
    else:
        return render(request, 'login/test.html')

@csrf_exempt
@login_required
def upd_user(request):
    if request.method == "POST":
        n_1 = {'status': '更新成功！'}
        n_2 = {'status': '更新失败！'}
        n_3 = {'status': '错误！'}
        # try:
        userID = request.POST.get('userid', None)
        # userSignature = request.POST.get('sign', None)
        # userPKOriginal = request.POST.get('password', None)
        userPKLatest = request.POST.get('publickey', None)
        print("userID: ", userID)
        pContent = request.POST.get('pContent', None)
        opType = request.POST.get('opType', None)
        sContent = request.POST.get('sContent', None)
        checkSum = request.POST.get('checkSum', None)

        accMsg = accessProtocol.accessProtocol(opType=opType, pContent=pContent, sContent=sContent,
                                               checkSum=checkSum)
        print("update accmsg: ", accMsg)

        checkSumValid = accMsg.checkSumValid()
        print("checkSumValid", checkSumValid)
        # try:
        #     userPubkey = R.search(R.root, userID)
        #     print("userpubkey: ", userPubkey)
        # sigValid = False
        #
        # if userPubkey != '':
        #     sigValid = sm2.Verify(sContent, pContent, userPubkey, 64)

        # if checkSumValid and sigValid:

        #     userAddress = UserInfo.objects.get(userID=userID).address
        #     print(userAddress)
        #     print(contractTAC.getID(addr=userAddress))
        # except:

        if checkSumValid:
            res = R.updatePubkey(R.root, userID, userPKLatest)
            resSqlite = UserInfo.objects.filter(userID=userID).update(pubkeyInfo=userPKLatest)
            print("resSqlite: ", resSqlite)
            print("updatekey : ", res)
            userAddress = UserInfo.objects.get(userID=userID, pubkeyInfo=userPKLatest).address
            print(contractTAC.getID(addr=userAddress))
            try:
                resUpdate = contractTAC.updatePubkey(addr=userAddress, pubkey=userPKLatest)
                print("resUpdate : ", resUpdate)
            except:
                print("resUpdate : ")

            if res :
                return HttpResponse(json.dumps(n_1), content_type='application/json')

        return HttpResponse(json.dumps(n_2), content_type='application/json')
    # except:
    #     return HttpResponse(json.dumps(n_3), content_type='application/json')
    else:
        return render(request, 'login/test.html')

@csrf_exempt
def jiami(request):
    if request.method == "POST":
        userID = request.POST.get('username', None)
        privateKey = request.POST.get('privatekey', None)
        print("privatekey: ", privateKey)
        sig = sm2.Sign(userID, privateKey, '12345678abcdef', 64)
        print("sig: ", sig.hex())
        return HttpResponse(json.dumps(sig.hex()), content_type='application/json')
    # else:
    #     return HttpResponse(json.dumps("SIGNATURE WRONG!"), content_type='application/json')

    return render(request, 'login/jiami.html')

@csrf_exempt
@login_required
def userVerify(request):
    if request.method == "POST":
        userID = request.POST.get('username', None)
        sigNature = request.POST.get('password', None)

        pContent = request.POST.get('pContent', None)
        opType = request.POST.get('opType', None)
        sContent = request.POST.get('sContent', None)
        checkSum = request.POST.get('checkSum', None)

        accMsg = accessProtocol.accessProtocol(opType=opType, pContent=pContent, sContent=sContent,
                                               checkSum=checkSum)
        print("update accmsg: ", accMsg)
        checkSumValid = accMsg.checkSumValid()
        print("checkSumValid", checkSumValid)
        userPubkey = R.search(R.root, userID)
        print("userpubkey: ", userPubkey)
        sigValid = False

        if userPubkey != '':
            sigValid = sm2.Verify(sigNature, pContent, userPubkey, 64)

        if checkSumValid:
            return HttpResponse(json.dumps(sigValid), content_type='application/json')
    return render(request, 'login/test.html')


