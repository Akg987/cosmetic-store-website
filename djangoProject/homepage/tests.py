from django.test import TestCase

# Create your tests here.
"""
<div style="background: #F2DCB1;border-radius: 30px;padding: 30px">
<div class="row">
{% for item in cosmetics %}
	 <div class="col-lg-4">
          <div class="item" style="background-color:#fff;position:relative;border-radius:25px;text-align:center;margin-bottom:40px;">
            <div class="thumb" style="position: relative;border-radius: 25px;overflow: hidden;">
              <a id="id_image" href="productdetails.html"><img src="{{ item.image.url }}" alt="{{ item.title }}"></a>
            </div>
            <div class="down-content">
                <span id="id_category" class="category">{{ item.category }}</span>
                <h4 id="id_title">{{ item.title }}</h4>
                <a href="productdetails.html">view</a>
            </div>
          </div>
        </div>

	{% endfor %}
</div>

</div>

listmyask = ask.objects.filter(user_id=user_st["User"].id).all()

$(".imggif2").hide()
    $(".savecontent").click(function() {
        $(".imggif").hide()
        $(".imggif2").show()
"""