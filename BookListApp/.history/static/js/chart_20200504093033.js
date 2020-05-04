
<script type="text/javascript">
window.onload = function () {
    var chart = new CanvasJS.Chart("chartContainer",
    {
    title:{
        text: "Books Read and Unread"
    },
    legend: {
        maxWidth: 350,
        itemWidth: 120
    },
    data: [
    {
        type: "pie",
        showInLegend: true,
        legendText: "{indexLabel}",
        dataPoints: [
        { y: 4, indexLabel: "Read" },
        { y: 2, indexLabel: "Unread" },
        ]
    }
    ]
    });
    chart.render();
}
</script>
<script type="text/javascript" src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>