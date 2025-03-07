


let menu = document.querySelector('#bars');
let navbar = document.querySelector('.navbar');
// menu.onclick = () =>{
//     menu.classList.toggle('fa-times');
//     menu.classList.toggle('active');
// }
// menu.addEventListener("click", () =>{
//     menu.classList.toggle('fa-times');
//     navbar.classList.toggle('active');
// })






function updateQuantity(operation,productId)
{
    const inputBox= document.getElementById("quantity"+productId);
    inputBox.value=parseInt(inputBox.value)+operation;

}

var swiper = new Swiper('.swiper-container',{
    pagination:{
        el:'.swiper-pagination',
    },
});

