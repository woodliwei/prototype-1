/*
 * 策略展示js 
 */

var avgOptions ={
    chart: {
        backgroundColor: '#fff',
        spacing: [0, 0, 0, 0],
        margin: [40, 20, 30, 80],
        renderTo: 'mainContainer'
    },
    rangeSelector : {
        selected : 0
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
            text : 'avg price'
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

var resultOptions ={
    chart: {
        backgroundColor: '#fff',
        spacing: [0, 0, 0, 0],
        margin: [40, 20, 30, 80],
        zoomType: 'x',
        renderTo: 'mainContainer'
    },
    rangeSelector : {
        selected : 1
    },
    title : {
        align: 'left',
        text: '',
        style: {
            fontSize: '12px',
            color: '#e7e7e7',
            fontWeight: 'bold'
        }
    },
    xAxis: [{
        type: 'datetime',
        dateTimeLabelFormats: {
            day: '%e of %b'
        },
        title: {
            text: null
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        gridLineDashStyle: 'dash',
        minTickInterval: 10
    }],
    yAxis: [{
        title: {
            text: '百分比 (%)'
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd'

    }],
    series : [{
        color: '#b51120',
        turboThreshold: 1440,
        marker: {
            enabled: false
        },
        tooltip: {
            valueDecimals: 2
        }
    }]
};

var chartOptions = {

    chart: {
        backgroundColor: '#fff',
        spacing: [0, 0, 0, 0],
        margin: [40, 20, 30, 80],
        zoomType: 'x',
        renderTo: 'mainContainer'
    },
    colors: [
        '#b51120',
        '#c83df2',
        '#fca508'
    ],
    title: {
        align: 'left',
        text: '',
        style: {
            fontSize: '12px',
            color: '#e7e7e7',
            fontWeight: 'bold'
        }
    },
    xAxis: [{
        type: 'datetime',
        dateTimeLabelFormats: {
            day: '%e of %b'
        },
        title: {
            text: null
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        gridLineDashStyle: 'dash',
        minTickInterval: 10
    }],
    yAxis: [{
        title: {
            text: '百分比 (%)'
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd'

    }],
    tooltip: {
        shared: false,      //是否公用同一个tooltip
        crosshairs: [true, true],
        borderRadius: 0,
        headerFormat: '',
        pointFormat: '<b><span style="color:{series.color}">时间：{point.category}<span></b>' +
                            '<br/><b><span style="color:{series.color}">百分比：{point.y}%<span></b>'
    },
    followTouchMove:{
        enalbed:true,
    },
    legend: {
        enabled: true,
        borderRadius: 0,
        borderColor: '#080808',
        align: 'left',
        verticalAlign: 'top',
        floating: true,
        margin: 10,
        useHtml: true,
        symbolWidth: 0,      //隐藏图例前面的横线
    },
    credits: {
        enabled: false
    },
    series: [{
        type: 'spline',
        color: '#b51120',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }

    }]
};

var latestOptions01 = {

    chart: {
        backgroundColor: '#fff',
        spacing: [0, 0, 0, 0],
        margin: [10, 0, 25, 0],
        renderTo: 'latestContainer01'
    },
    colors: [
        '#b51120',
        '#c83df2',
        '#fca508'
    ],
    title: {
        align: 'left',
        text: '',
        style: {
            fontSize: '12px',
            color: '#e7e7e7',
            fontWeight: 'bold'
        }
    },
    xAxis: [{
        type: 'datetime',
        dateTimeLabelFormats: {
            day: '%e of %b'
        },
        title: {
            text: null
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        gridLineDashStyle: 'dash',
        minTickInterval: 2,
        minorGridLineWidth: 1,
        minorGridLineColor: '#ddd',
        minorTickInterval: 1
    }],
    yAxis: [{
        title: {
            text: ''
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        offset: -40

    }],
    tooltip: {
        shared: false,      //是否公用同一个tooltip
        crosshairs: [true, true],
        borderRadius: 0,
        headerFormat: '',
        pointFormat: '<b><span style="color:{series.color}">时间：{point.category}<span></b>' +
                            '<br/><b><span style="color:{series.color}">百分比：{point.y}%<span></b>'
    },
    legend: {
        enabled: false,
        borderRadius: 0,
        borderColor: '#080808',
        align: 'left',
        verticalAlign: 'top',
        floating: true,
        margin: 10,
        useHtml: true,
        symbolWidth: 0,      //隐藏图例前面的横线
    },
    credits: {
        enabled: false
    },
    series: [{
        type: 'spline',
        color: '#b51120',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }

    }]
};

var latestOptions02 = {

    chart: {
        backgroundColor: '#fff',
        spacing: [0, 0, 0, 0],
        margin: [10, 0, 25, 0],
        renderTo: 'latestContainer02'
    },
    colors: [
        '#b51120',
        '#c83df2',
        '#fca508'
    ],
    title: {
        align: 'left',
        text: '',
        style: {
            fontSize: '12px',
            color: '#e7e7e7',
            fontWeight: 'bold'
        }
    },
    xAxis: [{
        type: 'datetime',
        dateTimeLabelFormats: {
            day: '%e of %b'
        },
        title: {
            text: null
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        gridLineDashStyle: 'dash',
        minTickInterval: 2,
        minorGridLineWidth: 1,
        minorGridLineColor: '#ddd',
        minorTickInterval: 1
    }],
    yAxis: [{
        title: {
            text: ''
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        offset: -40

    }],
    tooltip: {
        shared: false,      //是否公用同一个tooltip
        crosshairs: [true, true],
        borderRadius: 0,
        headerFormat: '',
        pointFormat: '<b><span style="color:{series.color}">时间：{point.category}<span></b>' +
                            '<br/><b><span style="color:{series.color}">百分比：{point.y}%<span></b>'
    },
    legend: {
        enabled: false,
        borderRadius: 0,
        borderColor: '#080808',
        align: 'left',
        verticalAlign: 'top',
        floating: true,
        margin: 10,
        useHtml: true,
        symbolWidth: 0,      //隐藏图例前面的横线
    },
    credits: {
        enabled: false
    },
    series: [{
        type: 'spline',
        color: '#b51120',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }

    }]
};


var latestOptions03 = {

    chart: {
        backgroundColor: '#fff',
        spacing: [0, 0, 0, 0],
        margin: [10, 0, 25, 0],
        renderTo: 'latestContainer03'
    },
    colors: [
        '#b51120',
        '#c83df2',
        '#fca508'
    ],
    title: {
        align: 'left',
        text: '',
        style: {
            fontSize: '12px',
            color: '#e7e7e7',
            fontWeight: 'bold'
        }
    },
    xAxis: [{
        type: 'datetime',
        dateTimeLabelFormats: {
            day: '%e of %b'
        },
        title: {
            text: null
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        gridLineDashStyle: 'dash',
        minTickInterval: 2,
        minorGridLineWidth: 1,
        minorGridLineColor: '#ddd',
        minorTickInterval: 1
    }],
    yAxis: [{
        title: {
            text: ''
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        offset: -40

    }],
    tooltip: {
        shared: false,      //是否公用同一个tooltip
        crosshairs: [true, true],
        borderRadius: 0,
        headerFormat: '',
        pointFormat: '<b><span style="color:{series.color}">时间：{point.category}<span></b>' +
                            '<br/><b><span style="color:{series.color}">百分比：{point.y}%<span></b>'
    },
    legend: {
        enabled: false,
        borderRadius: 0,
        borderColor: '#080808',
        align: 'left',
        verticalAlign: 'top',
        floating: true,
        margin: 10,
        useHtml: true,
        symbolWidth: 0,      //隐藏图例前面的横线
    },
    credits: {
        enabled: false
    },
    series: [{
        type: 'spline',
        color: '#b51120',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }

    }]
};


var latestOptions04 = {

    chart: {
        backgroundColor: '#fff',
        spacing: [0, 0, 0, 0],
        margin: [10, 0, 25, 0],
        renderTo: 'latestContainer04'
    },
    colors: [
        '#b51120',
        '#c83df2',
        '#fca508'
    ],
    title: {
        align: 'left',
        text: '',
        style: {
            fontSize: '12px',
            color: '#e7e7e7',
            fontWeight: 'bold'
        }
    },
    xAxis: [{
        type: 'datetime',
        dateTimeLabelFormats: {
            day: '%e of %b'
        },
        title: {
            text: null
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        gridLineDashStyle: 'dash',
        minTickInterval: 2,
        minorGridLineWidth: 1,
        minorGridLineColor: '#ddd',
        minorTickInterval: 1
    }],
    yAxis: [{
        title: {
            text: ''
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        offset: -40

    }],
    tooltip: {
        shared: false,      //是否公用同一个tooltip
        crosshairs: [true, true],
        borderRadius: 0,
        headerFormat: '',
        pointFormat: '<b><span style="color:{series.color}">时间：{point.category}<span></b>' +
                            '<br/><b><span style="color:{series.color}">百分比：{point.y}%<span></b>'
    },
    legend: {
        enabled: false,
        borderRadius: 0,
        borderColor: '#080808',
        align: 'left',
        verticalAlign: 'top',
        floating: true,
        margin: 10,
        useHtml: true,
        symbolWidth: 0,      //隐藏图例前面的横线
    },
    credits: {
        enabled: false
    },
    series: [{
        type: 'spline',
        color: '#b51120',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }

    }]
};


var topOptions01 = {

    chart: {
        backgroundColor: '#fff',
        spacing: [0, 0, 0, 0],
        margin: [10, 0, 25, 0],
        renderTo: 'topContainer01'
    },
    colors: [
        '#b51120',
        '#c83df2',
        '#fca508'
    ],
    title: {
        align: 'left',
        text: '',
        style: {
            fontSize: '12px',
            color: '#e7e7e7',
            fontWeight: 'bold'
        }
    },
    xAxis: [{
        type: 'datetime',
        dateTimeLabelFormats: {
            day: '%e of %b'
        },
        title: {
            text: null
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        gridLineDashStyle: 'dash',
        minTickInterval: 2,
        minorGridLineWidth: 1,
        minorGridLineColor: '#ddd',
        minorTickInterval: 1
    }],
    yAxis: [{
        title: {
            text: ''
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        offset: -40

    }],
    tooltip: {
        shared: false,      //是否公用同一个tooltip
        crosshairs: [true, true],
        borderRadius: 0,
        headerFormat: '',
        pointFormat: '<b><span style="color:{series.color}">时间：{point.category}<span></b>' +
                            '<br/><b><span style="color:{series.color}">百分比：{point.y}%<span></b>'
    },
    legend: {
        enabled: false,
        borderRadius: 0,
        borderColor: '#080808',
        align: 'left',
        verticalAlign: 'top',
        floating: true,
        margin: 10,
        useHtml: true,
        symbolWidth: 0,      //隐藏图例前面的横线
    },
    credits: {
        enabled: false
    },
    series: [{
        type: 'spline',
        color: '#b51120',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }

    }]
};

var topOptions02 = {

    chart: {
        backgroundColor: '#fff',
        spacing: [0, 0, 0, 0],
        margin: [10, 0, 25, 0],
        renderTo: 'topContainer02'
    },
    colors: [
        '#b51120',
        '#c83df2',
        '#fca508'
    ],
    title: {
        align: 'left',
        text: '',
        style: {
            fontSize: '12px',
            color: '#e7e7e7',
            fontWeight: 'bold'
        }
    },
    xAxis: [{
        type: 'datetime',
        dateTimeLabelFormats: {
            day: '%e of %b'
        },
        title: {
            text: null
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        gridLineDashStyle: 'dash',
        minTickInterval: 2,
        minorGridLineWidth: 1,
        minorGridLineColor: '#ddd',
        minorTickInterval: 1
    }],
    yAxis: [{
        title: {
            text: ''
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        offset: -40

    }],
    tooltip: {
        shared: false,      //是否公用同一个tooltip
        crosshairs: [true, true],
        borderRadius: 0,
        headerFormat: '',
        pointFormat: '<b><span style="color:{series.color}">时间：{point.category}<span></b>' +
                            '<br/><b><span style="color:{series.color}">百分比：{point.y}%<span></b>'
    },
    legend: {
        enabled: false,
        borderRadius: 0,
        borderColor: '#080808',
        align: 'left',
        verticalAlign: 'top',
        floating: true,
        margin: 10,
        useHtml: true,
        symbolWidth: 0,      //隐藏图例前面的横线
    },
    credits: {
        enabled: false
    },
    series: [{
        type: 'spline',
        color: '#b51120',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }

    }]
};


var topOptions03 = {

    chart: {
        backgroundColor: '#fff',
        spacing: [0, 0, 0, 0],
        margin: [10, 0, 25, 0],
        renderTo: 'topContainer03'
    },
    colors: [
        '#b51120',
        '#c83df2',
        '#fca508'
    ],
    title: {
        align: 'left',
        text: '',
        style: {
            fontSize: '12px',
            color: '#e7e7e7',
            fontWeight: 'bold'
        }
    },
    xAxis: [{
        type: 'datetime',
        dateTimeLabelFormats: {
            day: '%e of %b'
        },
        title: {
            text: null
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        gridLineDashStyle: 'dash',
        minTickInterval: 2,
        minorGridLineWidth: 1,
        minorGridLineColor: '#ddd',
        minorTickInterval: 1
    }],
    yAxis: [{
        title: {
            text: ''
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        offset: -40

    }],
    tooltip: {
        shared: false,      //是否公用同一个tooltip
        crosshairs: [true, true],
        borderRadius: 0,
        headerFormat: '',
        pointFormat: '<b><span style="color:{series.color}">时间：{point.category}<span></b>' +
                            '<br/><b><span style="color:{series.color}">百分比：{point.y}%<span></b>'
    },
    legend: {
        enabled: false,
        borderRadius: 0,
        borderColor: '#080808',
        align: 'left',
        verticalAlign: 'top',
        floating: true,
        margin: 10,
        useHtml: true,
        symbolWidth: 0,      //隐藏图例前面的横线
    },
    credits: {
        enabled: false
    },
    series: [{
        type: 'spline',
        color: '#b51120',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }

    }]
};


var topOptions04 = {

    chart: {
        backgroundColor: '#fff',
        spacing: [0, 0, 0, 0],
        margin: [10, 0, 25, 0],
        renderTo: 'topContainer04'
    },
    colors: [
        '#b51120',
        '#c83df2',
        '#fca508'
    ],
    title: {
        align: 'left',
        text: '',
        style: {
            fontSize: '12px',
            color: '#e7e7e7',
            fontWeight: 'bold'
        }
    },
    xAxis: [{
        type: 'datetime',
        dateTimeLabelFormats: {
            day: '%e of %b'
        },
        title: {
            text: null
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        gridLineDashStyle: 'dash',
        minTickInterval: 2,
        minorGridLineWidth: 1,
        minorGridLineColor: '#ddd',
        minorTickInterval: 1
    }],
    yAxis: [{
        title: {
            text: ''
        },
        gridLineWidth: 1,
        gridLineColor: '#ddd',
        offset: -40

    }],
    tooltip: {
        shared: false,      //是否公用同一个tooltip
        crosshairs: [true, true],
        borderRadius: 0,
        headerFormat: '',
        pointFormat: '<b><span style="color:{series.color}">时间：{point.category}<span></b>' +
                            '<br/><b><span style="color:{series.color}">百分比：{point.y}%<span></b>'
    },
    legend: {
        enabled: false,
        borderRadius: 0,
        borderColor: '#080808',
        align: 'left',
        verticalAlign: 'top',
        floating: true,
        margin: 10,
        useHtml: true,
        symbolWidth: 0,      //隐藏图例前面的横线
    },
    credits: {
        enabled: false
    },
    series: [{
        type: 'spline',
        color: '#b51120',
        turboThreshold: 1440,
        marker: {
            enabled: false
        }

    }]
};

$(function () {

    queryData();
    //var chartTimer = setInterval(function () {
    //    queryData();
    //}, 60 * 1000);

    queryLatestData();
    //var latestTimer = setInterval(function () {
    //    queryLatestData();
    //}, 60 * 1000);

    queryTopData();
    //var latestTimer = setInterval(function () {
    //    queryTopData();
    //}, 60 * 1000);

});


//获取url参数
function getQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]); return null;
}


//请求最新策略
function queryLatestData() {

    $.ajax({
        url: dataUrlBase + 'latestData.html',
        type: 'get',
        //dataType:'json',
        success: function (dts) {
            dts = eval('(' + dts + ')');    //当请求类型为json类型时，这句代码可注释

            var s1Data = dts[0].s1[0];
            var s2Data = dts[0].s2[0];
            var s3Data = dts[0].s3[0];
            var s4Data = dts[0].s4[0];

            latestOptions01.series[0].name = s1Data.name;
            latestOptions02.series[0].name = s2Data.name;
            latestOptions03.series[0].name = s3Data.name;
            latestOptions04.series[0].name = s4Data.name;

            //策略名称
            $('#latestSName01').html(s1Data.name);
            $('#latestSName02').html(s2Data.name);
            $('#latestSName03').html(s3Data.name);
            $('#latestSName04').html(s4Data.name);

            latestOptions01.series[0].data = s1Data.vals;
            latestOptions02.series[0].data = s2Data.vals;
            latestOptions03.series[0].data = s3Data.vals;
            latestOptions04.series[0].data = s4Data.vals;

            //策略当前值
            var lastVal01 = s1Data.vals[s1Data.vals.length - 1];
            var lastVal02 = s2Data.vals[s2Data.vals.length - 1];
            var lastVal03 = s3Data.vals[s3Data.vals.length - 1];
            var lastVal04 = s4Data.vals[s4Data.vals.length - 1];
            $('#latestVal01').html('当前百分比：' + lastVal01);
            $('#latestVal02').html('当前百分比：' + lastVal02);
            $('#latestVal03').html('当前百分比：' + lastVal03);
            $('#latestVal04').html('当前百分比：' + lastVal04);

            latestOptions01.xAxis[0].categories = s1Data.categories;
            latestOptions02.xAxis[0].categories = s2Data.categories;
            latestOptions03.xAxis[0].categories = s3Data.categories;
            latestOptions04.xAxis[0].categories = s4Data.categories;

            latestChart01 = new Highcharts.Chart(latestOptions01);
            latestChart02 = new Highcharts.Chart(latestOptions02);
            latestChart03 = new Highcharts.Chart(latestOptions03);
            latestChart04 = new Highcharts.Chart(latestOptions04);
        }
    });
}

//请求策略排行数据
function queryTopData() {

    $.ajax({
        url: dataUrlBase +'topData.html',
        type: 'get',
        //dataType:'json',
        success: function (dts) {
            dts = eval('(' + dts + ')');    //当请求类型为json类型时，这句代码可注释

            var s1Data = dts[0].s1[0];
            var s2Data = dts[0].s2[0];
            var s3Data = dts[0].s3[0];
            var s4Data = dts[0].s4[0];

            topOptions01.series[0].name = s1Data.name;
            topOptions02.series[0].name = s2Data.name;
            topOptions03.series[0].name = s3Data.name;
            topOptions04.series[0].name = s4Data.name;

            //策略名称
            $('#topSName01').html(s1Data.name);
            $('#topSName02').html(s2Data.name);
            $('#topSName03').html(s3Data.name);
            $('#topSName04').html(s4Data.name);

            topOptions01.series[0].data = s1Data.vals;
            topOptions02.series[0].data = s2Data.vals;
            topOptions03.series[0].data = s3Data.vals;
            topOptions04.series[0].data = s4Data.vals;

            //策略当前值
            var topVal01 = s1Data.vals[s1Data.vals.length - 1];
            var topVal02 = s2Data.vals[s2Data.vals.length - 1];
            var topVal03 = s3Data.vals[s3Data.vals.length - 1];
            var topVal04 = s4Data.vals[s4Data.vals.length - 1];
            $('#topVal01').html('当前百分比：' + topVal01);
            $('#topVal02').html('当前百分比：' + topVal02);
            $('#topVal03').html('当前百分比：' + topVal03);
            $('#topVal04').html('当前百分比：' + topVal04);

            topOptions01.xAxis[0].categories = s1Data.categories;
            topOptions02.xAxis[0].categories = s2Data.categories;
            topOptions03.xAxis[0].categories = s3Data.categories;
            topOptions04.xAxis[0].categories = s4Data.categories;

            topChart01 = new Highcharts.Chart(topOptions01);
            topChart02 = new Highcharts.Chart(topOptions02);
            topChart03 = new Highcharts.Chart(topOptions03);
            topChart04 = new Highcharts.Chart(topOptions04);
        }
    });
}
