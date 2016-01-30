/*
 * regression test result chart
 */

var resultOptions ={
    chart: {
        backgroundColor: '#fff',
        spacing: [0, 0, 0, 0],
        margin: [10, 0, 25, 0],
        pinchType:'None'
    },
    title : {
        text : ''
    },
    tooltip: {
        style: {
            width: '200px'
        },
        valueDecimals: 4,
        shared : true
    },
    xAxis: {
        type: 'datetime',
        dateTimeLabelFormats: { // don't display the dummy year
                month: '%e. %b',
                year: '%b'
        }
    },
    yAxis : {
        title : {
            text : 'value'
        }
    },
    series: [{
        type: 'spline',
        color: '#b51120',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }
    }, {
        type: 'spline',
        color: '#c83df2',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }
    }
    ]
}


