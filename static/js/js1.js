$( document ).ready(function(){

  $('#a').click(function() {
    console.log("Add");
    $(this).css({
      'background-color': 'yellow',
      'width': '400px',
      'height': '400px'
    });
    });
  });
