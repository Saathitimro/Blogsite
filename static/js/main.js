var toggle = false;

function showOption(){
	var list = document.querySelector('#option');
	if( list.style.display == "block" ){
		list.style.display = 'none';
		toggle = true;
	}else{
		list.style.display = 'block';
		toggle = false;
	}
}

window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    if(scrolled>=100){
        document.querySelector("#underlayimg").style.filter = "brightness(70%) blur(4px)";
    }else{
        document.querySelector("#underlayimg").style.filter = "brightness(70%)";
    }
    // console.log(scrolled);
});

var slideIndex = 0;

carousel();

function carousel() {
  var i;
  var slides = document.getElementsByClassName("overlay");
  for(i= 0; i< slides.length; i++){
    slides[i].style.display = "none";
    console.log(slides.length);
  }
  slideIndex++;
  if(slideIndex > slides.length){
    slideIndex = 1;
  }
  slides[slideIndex-1].style.display = "flex";
  setTimeout(carousel, 15000);
}