$(function() {

	function get_window_dimensions() {
	    var win_h = $("#display_port").height();
	    var win_w = $("#display_port").width();
	    return [win_h, win_w];
	}

	function get_guy_dimensions() {
	    var guy_height = $("#guy_icon").height();
	    var guy_width = $("#guy_icon").width();
	    return [guy_height, guy_width];
	}

	function place_guy() {
	    var win_dimensions = get_window_dimensions();
	    var window_h = win_dimensions[0];
	    var window_w = win_dimensions[1];
	    var window_center_h = window_h / 2;
	    var window_center_w = window_w / 2;

	    
	    var guy_dimensions = get_guy_dimensions();
	    var guy_h = guy_dimensions[0];
	    var guy_w = guy_dimensions[1];
	    var guy_h_offset = guy_h / 2;
	    var guy_w_offset = guy_w / 2;

	    var guy_top = window_center_h - (guy_pos_y * guy_h) - guy_h_offset;
	    var guy_left = window_center_w + (guy_pos_x * guy_w) - guy_w_offset;

	    $("#guy_icon").parent().css({'position': 'relative'});
	    $("#guy_icon").css({'top': guy_top, 'left': guy_left, 'position': 'absolute'});
	    $("#guy_icon").attr('title', function() {
		    return '.ui-icon-circle-triangle-' + guy_dir;
		});
	    $("#guy_icon span").addClass(function() {
		    return 'ui-icon-circle-triangle-' + guy_dir;
		});

	}

	place_guy();

	$(".move_button").click(function(event) {
		var command = $(this).attr("id");
		var url = "/guy/" + guy_id + "/c/" + command + "/";
		location.replace(url);
	    });

});