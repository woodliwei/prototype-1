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
    global: {
        timezoneOffset: -8 * 60  // +8 时区修正方法
    },
    lang:{
        months:['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月',  '十月', '十一月', '十二月'],
        shortMonths: [ '1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月',  '10月', '11月', '12月'],
        weekdays:['星期日',  '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
    },
    legend: {
        layout: 'vertical',
        backgroundColor: '#FFFFFF',
        floating: true,
        align: 'center',
        verticalAlign: 'top',
        enabled: true
    },
    rangeSelector: {
        buttons: [{//定义一组buttons,下标从0开始
            type: 'week',
            count: 1,
            text: '1周'
            },
            {
            type: 'month',
            count: 1,
            text: '1月'
            },
            {
            type: 'month',
            count: 3,
            text: '3月'
            },
            {
            type: 'month',
            count: 6,
            text: '6月'
            },
            {
            type: 'ytd',
            text: '1季度'
            },
            {
            type: 'year',
            count: 1,
            text: '1年'
            },
            {
            type: 'all',
            text: '全部'
        }],
        buttonTheme: {
            width: 36,
            height: 16,
            padding: 1,
            r: 0,
            stroke: '#68A',
            zIndex: 7
            },
        inputDateFormat: '%Y-%m-%d',
        inputEditDateFormat: '%Y-%m-%d',
    },
    xAxis: {
        type: 'datetime',
        dateTimeLabelFormats: {
            day: '%Y-%m-%d'
        },
        title: {
            text: null
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        gridLineDashStyle: 'dash',
        minTickInterval: 10
    },
    yAxis : {
        title : {
            text : 'value'
        }
    },
    series: [{
        color: '#b51120',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }
    }, {
        color: '#c83df2',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }
    }
    ]
}


