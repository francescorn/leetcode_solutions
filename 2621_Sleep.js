/**
 * @param {number} millis
 */
async function sleep(millis) {
     const p = new Promise(res => setTimeout(res, millis));
     return p;
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
