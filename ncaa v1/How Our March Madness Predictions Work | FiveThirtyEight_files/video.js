jQuery(document).ready(function(o){var t=o(window);0<o("video[data-defer=play]").length&&t.on("scroll.deferredvideos",_.throttle(function(){o("video[data-defer=play]").each(function(e,d){t.scrollTop()>o(d).offset().top-300&&(o(d).attr("data-defer","none"),d.play())}),0===o("video[data-defer=play]").length&&t.off("scroll.deferredvideos")}))});