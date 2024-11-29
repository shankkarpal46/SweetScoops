


let menu = document.querySelector('#bars');
let navbar = document.querySelector('.navbar');
// menu.onclick = () =>{
//     menu.classList.toggle('fa-times');
//     menu.classList.toggle('active');
// }


menu.addEventListener("click", () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
})

document.querySelectorAll('.top-image').forEach(image_1 =>{
    image_1.addEventListener('click',() =>{
        var src = image_1.getAttribute('src');
        document.querySelector('.big-image1').src = src;
        // document.querySelector('.big-image1').src = src;
    });
});


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

