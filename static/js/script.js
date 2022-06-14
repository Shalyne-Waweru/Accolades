$(document).ready(function(){

  $('.close').click(function(){
    $('.alert').css("display", "none");
  })

})

const allStars = document.querySelectorAll('.d-star');
let current_rating = document.querySelector('.current_rating')


allStars.forEach( (star, i) =>{
  star.onclick = function(){
    // Current Level of clicked star
    let current_star_level = i + 1;
    // current_rating.innerText = `${current_star_level} of 10`;
    current_rating.innerHTML = current_star_level + " of 10";
    current_rating.style.fontWeight = "bold";

    allStars.forEach( (star, j) => {
      // Color the stars
      if(current_star_level >= j + 1){
        star.innerHTML = '&#9733'
      }
      // Discolor the stars
      else{
        star.innerHTML = '&#9734'
      }
    })
  }
})