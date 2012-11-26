window.utils =
  loadTemplate: (app, views, callback) ->
    deferreds = []
    $.each views, (index, v) ->
      if window[v]
        deferreds.push $.get("/static/tpl/" + v + ".html", (data) ->
          window[v]::template = swig.compile(data)
        )

    $.when.apply(null, deferreds).done callback
