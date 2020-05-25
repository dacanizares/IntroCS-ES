
$(function() {
  // Smooth scroll handler
  $('a').on('click', function(event) {

    if (!this.hash)
      return;

    event.preventDefault();

    let target = this.hash;
    $('html, body').animate({
      scrollTop: $(target).offset().top
    }, 800, function(){
      // Update URL
      window.location.hash = target;
    });
  });
});
