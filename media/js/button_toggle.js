/*
 * Button Toggle 
 *
 * From Tianwei
 *
 * 
 */

$.fn.btn_toggle = function(){

  $(this).click(
    function(){
      
      var label = "#" + $(this).attr("control_id");

      if($(label).attr("visible")=="false")
        {
          $(this).text("undo this choice");
          $(label).attr("visible","true"); 
          $(label).show();
        }
      else
        {
          $(this).text("please choice");
          $(label).attr("visible","false"); 
          $(label).hide();
        }
  });

};
