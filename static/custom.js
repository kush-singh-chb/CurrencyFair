$(window).ready(function () {
    //get currency abbrevations
    $.ajax({
        url: '/getCurrency',
        type: 'GET',
        contentType: 'application/json;charset=UTF-8',
        dataType: "json",
        success: function (data) {
            console.log(data)
            data.forEach(function (item) {
                $("#from_Currency").append(new Option(item, item))
                $("#to_Currency").append(new Option(item, item))
            })
        }
    });
});

var st = null

function stop_rt() {
    //stopping continuous api fetching
    console.log("Stopping rt")
    if (st != null)
        clearInterval(st)
}

function load_graph() {
    // check if data is incorrect or missing or if to and from is same
    if (($("#from_Currency").val() !== $("#to_Currency").val()) && $("#from_Currency").val() !== null && $("#to_Currency").val() !== null) {
        //calling api async
        $.ajax({
            url: '/graph',
            type: 'GET',
            contentType: 'application/json;charset=UTF-8',
            dataType: "json",
            data: {
                'to': $("#to_Currency").val(),
                'from': $("#from_Currency").val()

            },
            //success callback
            success: function (data) {
                var plot_data = [
                    {
                        x: data.map(function (item) {
                            return item.timePlaced
                        }),
                        y: data.map(function (item) {
                            return item.rate
                        }),
                        type: 'scatter'
                    }
                ];
                Plotly.newPlot('plot', plot_data);
                st = setTimeout(load_graph, 500)
            },
            //error callback
            error: function (data) {
                alert(data.responseText)
            }
        })
        //response by validation
    } else if ($("#from_Currency").val() === $("#to_Currency").val()) {
        alert("Sorry,From and To Currency Cannot be Same")
    } else if ($("#from_Currency").val() === null) {
        alert("From value is empty")
    } else {
        alert("to value is empty")
    }

}