let pass1=document.querySelector(".pwd1");
let pass2=document.querySelector(".re-pwd1");
let submit=document.querySelector(".btnRegister");
let c=0;
submit.addEventListener('click',()=>{
    if(pass1.length==pass2.length){
        for(let i=0;i<pass1.length;i++){
            if(pass1.value.charAt(i)===pass2.value.charAt(i)){
                continue
            }
            else{
                c=1;
            }
        }
        if(c==1){
            alert("Password does not match");
        }
        else{
            console.log("Valid password");
        }
    }
    else{
        alert("Password does not match");
    }
})
