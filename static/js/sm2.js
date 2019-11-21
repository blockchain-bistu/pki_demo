/**
 * [SM2Encrypt description]
 * @param {[type]} data       [待加密数据]
 * @param {[type]} publickey  [公钥 hex]
 * @param {[type]} cipherMode [加密模式 C1C3C2:1, C1C2C3:0]
 * @return {[type]}           [返回加密后的数据 hex]
 */
function sm2Encrypt(data, publickey, cipherMode) {
    cipherMode = cipherMode == 0 ? cipherMode : 1;
    //msg = SM2.utf8tob64(msg);
    var msgData = CryptoJS.enc.Utf8.parse(data);

    var pubkeyHex = publickey;
    if (pubkeyHex.length > 64 * 2) {
        pubkeyHex = pubkeyHex.substr(pubkeyHex.length - 64 * 2);
    }

    var xHex = pubkeyHex.substr(0, 64);
    var yHex = pubkeyHex.substr(64);


    var cipher = new SM2Cipher(cipherMode);
    var userKey = cipher.CreatePoint(xHex, yHex);

    msgData = cipher.GetWords(msgData.toString());

    var encryptData = cipher.Encrypt(userKey, msgData);
    return '04' + encryptData;
}

/**
 * [SM2Decrypt sm2 解密数据]
 * @param {[type]} encrypted  [待解密数据 hex]
 * @param {[type]} privateKey [私钥 hex]
 * @param {[type]} cipherMode [加密模式 C1C3C2:1, C1C2C3:0]
 * @return {[type]}           [返回解密后的数据]
 */

function sm2Decrypt(encrypted, privateKey, cipherMode) {
    cipherMode = cipherMode == 0 ? cipherMode : 1;
    encrypted = encrypted.substr(2);
    //privateKey = b64tohex(privateKey);
    var privKey = new BigInteger(privateKey, 16);
    var cipher = new SM2Cipher(cipherMode);
    var decryptData = cipher.Decrypt(privKey, encrypted);
    return decryptData;
}

/**
 * [certCrypt 证书加密]
 * @param  {[type]} data       [加密数据]
 * @param  {[type]} certData   [证书 base64]
 * @param  {[type]} cipherMode [加密模式 C1C3C2:1, C1C2C3:0]
 * @return {[type]}            [返回加密后的数据 hex]
 */
function sm2CertCrypt(data, certData, cipherMode) {
    cipherMode = cipherMode == 0 ? cipherMode : 1;
    var key = "";
    //证书数据
    if (certData != "") {
        //通过证书获取key
        key = X509.getPublicKeyFromCertPEM(certData);
    }

    var pubkey = key.replace(/\s/g, '');


    var pubkeyHex = pubkey;
    if (pubkeyHex.length > 64 * 2) {
        pubkeyHex = pubkeyHex.substr(pubkeyHex.length - 64 * 2);
    }

    var xHex = pubkeyHex.substr(0, 64);
    var yHex = pubkeyHex.substr(64);


    var cipher = new SM2Cipher(cipherMode);
    var userKey = cipher.CreatePoint(xHex, yHex);

    var msgData = CryptoJS.enc.Utf8.parse(data);
    msgData = cipher.GetWords(msgData.toString());

    var encryptData = cipher.Encrypt(userKey, msgData);
    return encryptData;
}