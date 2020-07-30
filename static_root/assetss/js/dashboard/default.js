
//market-chart
new Chartist.Bar('.market-chart', {
    labels: ['100', '200', '300', '400', '500', '600', '700', '800'],
    series: [
        [5.3, 4, 3, 2, 3.5, 1.8, 3.8, 1.5],
        [2.8, 3, 4.3, 5, 2.9, 2.8, 2.8, 2.8]
    ]
},
    {
    seriesBarDistance: 2,
    chartPadding: {
        left: 0,
        right: 0,
        bottom: 0,
    },
    axisX: {
        showGrid: false,
        labelInterpolationFnc: function(value) {
            return value[0];
        }
    }
}, [
    ['screen and (min-width: 300px)', {
        seriesBarDistance: 15,
        axisX: {
            labelInterpolationFnc: function(value) {
                return value.slice(0, 3);
            }
        }
    }],
    ['screen and (min-width: 600px)', {
        seriesBarDistance: 12,
        axisX: {
            labelInterpolationFnc: Chartist.noop
        }
    }]
]).on('draw', function(ctx) {
    if(ctx.type === 'bar') {
        ctx.element.attr({
            x1: ctx.x1 + 0.05,
            style: 'stroke-linecap: round'
        });
    }
});


// vector map
! function(maps) {
    "use strict";
    var b = function() {};
    b.prototype.init = function() {
        maps("#world").vectorMap({
            map: "world_mill_en",
            scaleColors: ["#00baf2", "#1B8BF9"],
            normalizeFunction: "polynomial",
            hoverOpacity: .7,
            hoverColor: !1,
            regionStyle: {
                initial: {
                    fill: '#00baf2'
                }
            },
            markers: [
                { latLng: [23.30, 77.36], name: 'bhopal', style: {r: 8, fill:'white'}},
                { latLng: [24.774, 46.73], name: 'saudi Arbia', style: {r: 8, fill:'white'}},
                { latLng: [43.238949, 76.889709], name: 'Kazakstan', style: {r: 8, fill:'white'}},
                { latLng: [53.278046, -110.005470], name: 'Canada', style: {r: 8, fill:'white'}},
                { latLng: [14.23, 51.92], name: 'Brazil', style: {r: 8, fill:'white'}},
                { latLng: [64.11, 51.43], name: 'Greenland', style: {r: 8, fill:'white'}},
                { latLng: [69.19, 88.13], name: 'Russia', style: {r: 8, fill:'white'}}
            ],
            series: {
                regions: [{
                    scale: ['#00baf2', '#314da7'],
                    normalizeFunction: 'polynomial',
                    values: {
                        "AF": 16.63,
                        "AL": 11.58,
                        "DZ": 158.97,
                        "AO": 85.81,
                        "AG": 1.1,
                        "AR": 351.02,
                        "AM": 8.83,
                        "AU": 1219.72,
                        "AT": 366.26,
                        "AZ": 52.17,
                        "BS": 7.54,
                        "BH": 21.73,
                        "BD": 105.4,
                        "BB": 3.96,
                        "BY": 52.89,
                        "BE": 461.33,
                        "BZ": 1.43,
                        "BJ": 6.49,
                        "BT": 1.4,
                        "BO": 19.18,
                        "BA": 16.2,
                        "BW": 12.5,
                        "BR": 2023.53,
                        "BN": 11.96,
                        "BG": 44.84,
                        "BF": 8.67,
                        "BI": 1.47,
                        "KH": 11.36,
                        "CM": 21.88,
                        "CA": 1563.66,
                        "CV": 1.57,
                        "CF": 2.11,
                        "TD": 7.59,
                        "CL": 199.18,
                        "CN": 5745.13,
                        "CO": 283.11,
                        "KM": 0.56,
                        "CD": 12.6,
                        "CG": 11.88,
                        "CR": 35.02,
                        "CI": 22.38,
                        "HR": 59.92,
                        "CY": 22.75,
                        "CZ": 195.23,
                        "DK": 304.56,
                        "DJ": 1.14,
                        "DM": 0.38,
                        "DO": 50.87,
                        "EC": 61.49,
                        "EG": 216.83,
                        "SV": 21.8,
                        "GQ": 14.55,
                        "ER": 2.25,
                        "EE": 19.22,
                        "ET": 30.94,
                        "FJ": 3.15,
                        "FI": 231.98,
                        "FR": 2555.44,
                        "GA": 12.56,
                        "GM": 1.04,
                        "GE": 11.23,
                        "DE": 3305.9,
                        "GH": 18.06,
                        "GR": 305.01,
                        "GD": 0.65,
                        "GT": 40.77,
                        "GN": 4.34,
                        "GW": 0.83,
                        "GY": 2.2,
                        "HT": 6.5,
                        "HN": 15.34,
                        "HK": 226.49,
                        "HU": 132.28,
                        "IS": 12.77,
                        "IN": 1430.02,
                        "ID": 695.06,
                        "IR": 337.9,
                        "IQ": 84.14,
                        "IE": 204.14,
                        "IL": 201.25,
                        "IT": 2036.69,
                        "JM": 13.74,
                        "JP": 5390.9,
                        "JO": 27.13,
                        "KZ": 129.76,
                        "KE": 32.42,
                        "KI": 0.15,
                        "KR": 986.26,
                        "KW": 117.32,
                        "KG": 4.44,
                        "LA": 6.34,
                        "LV": 23.39,
                        "LB": 39.15,
                        "LS": 1.8,
                        "LR": 0.98,
                        "LY": 77.91,
                        "LT": 35.73,
                        "LU": 52.43,
                        "MK": 9.58,
                        "MG": 8.33,
                        "MW": 5.04,
                        "MY": 218.95,
                        "MV": 1.43,
                        "ML": 9.08,
                        "MT": 7.8,
                        "MR": 3.49,
                        "MU": 9.43,
                        "MX": 1004.04,
                        "MD": 5.36,
                        "MN": 5.81,
                        "ME": 3.88,
                        "MA": 91.7,
                        "MZ": 10.21,
                        "MM": 35.65,
                        "NA": 11.45,
                        "NP": 15.11,
                        "NL": 770.31,
                        "NZ": 138,
                        "NI": 6.38,
                        "NE": 5.6,
                        "NG": 206.66,
                        "NO": 413.51,
                        "OM": 53.78,
                        "PK": 174.79,
                        "PA": 27.2,
                        "PG": 8.81,
                        "PY": 17.17,
                        "PE": 153.55,
                        "PH": 189.06,
                        "PL": 438.88,
                        "PT": 223.7,
                        "QA": 126.52,
                        "RO": 158.39,
                        "RU": 1476.91,
                        "RW": 5.69,
                        "WS": 0.55,
                        "ST": 0.19,
                        "SA": 434.44,
                        "SN": 12.66,
                        "RS": 38.92,
                        "SC": 0.92,
                        "SL": 1.9,
                        "SG": 217.38,
                        "SK": 86.26,
                        "SI": 46.44,
                        "SB": 0.67,
                        "ZA": 354.41,
                        "ES": 1374.78,
                        "LK": 48.24,
                        "KN": 0.56,
                        "LC": 1,
                        "VC": 0.58,
                        "SD": 65.93,
                        "SR": 3.3,
                        "SZ": 3.17,
                        "SE": 444.59,
                        "CH": 522.44,
                        "SY": 59.63,
                        "TW": 426.98,
                        "TJ": 5.58,
                        "TZ": 22.43,
                        "TH": 312.61,
                        "TL": 0.62,
                        "TG": 3.07,
                        "TO": 0.3,
                        "TT": 21.2,
                        "TN": 43.86,
                        "TR": 729.05,
                        "TM": 0,
                        "UG": 17.12,
                        "UA": 136.56,
                        "AE": 239.65,
                        "GB": 2258.57,
                        "US": 14624.18,
                        "UY": 40.71,
                        "UZ": 37.72,
                        "VU": 0.72,
                        "VE": 285.21,
                        "VN": 101.99,
                        "YE": 30.02,
                        "ZM": 15.69,
                        "ZW": 5.57
                    }
                }]
            },
            backgroundColor: "transparent",
        })
    }, maps.VectorMap = new b, maps.VectorMap.Constructor = b
}(window.jQuery),
    function(maps) {
        "use strict";
        maps.VectorMap.init()
    }(window.jQuery);


// new customer

var optionsearningchart = {
    chart: {
        height: 400,
        type: 'radialBar',


    },
    plotOptions: {
        radialBar: {
            hollow: {
                margin: 20,
                size: "50%"
            },
            startAngle: -135,
            endAngle: 135,
            dataLabels: {
                name: {
                    fontSize: '16px',
                    color: '#314da7',
                    offsetY: 10
                },
                value: {
                    offsetY: -40,
                    fontSize: '22px',
                    color: '#314da7',
                    formatter: function (val) {
                        return val + "/100";
                    }
                }
            }
        }
    },

    fill: {
        opacity: 1
    },
    colors:['#314da7'],

    stroke: {
        dashArray: 4
    },
    series: [8*10],
    labels: ['Customer Ratio'],



}

var chartearningchart = new ApexCharts(
    document.querySelector("#customers"),
    optionsearningchart
);
chartearningchart.render();

// revenue chart
new Chartist.Bar('.revenue-chart', {
    labels: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
    series: [
        [400, 580, 200, 450, 650, 400, null, null, null, null, null],
        [null, null, null, null, null, null, 500, 300, 480, 600, 350]
    ],
}, {
    stackBars: true,
    chartPadding: {
        left: 0
    },
    axisY: {
        labelInterpolationFnc: function(value) {
            return (value / 1000) + 'k';
        },
        showLabel: false,
        showGrid: false,
        offset: 0,
    },
    axisX: {
        showGrid: false,
    }

}).on('draw', function(ctx) {
    if(ctx.type === 'bar') {
        ctx.element.attr({
            x1: ctx.x1 + 0.05,
            style: 'stroke-width: 15px ; stroke-linecap: round'
        });
    }
});


// btn js
$('.btn-js').click(function(){
    //make all inactive-doesn't work
    $( '.btn-js' ).each(function( ) {
        if($(this).hasClass('active')){
            $(this).removeClass('active')
        }
    });

    if($(this).hasClass('active')){
        $(this).removeClass('active')
    } else {
        $(this).addClass('active')
    }
});

$('.btn-js1').click(function(){
    $( '.btn-js1' ).each(function( ) {
        if($(this).hasClass('active')){
            $(this).removeClass('active')
        }
    });

    if($(this).hasClass('active')){
        $(this).removeClass('active')
    } else {
        $(this).addClass('active')
    }
});

// buy sell chart
if ($("#multiple-real-timeupdate ").length > 0) {
    var a = [],
        b = 300,
        c = function() {
            for (a.length > 0 && (a = a.slice(1)); a.length < b;) {
                var c = a.length > 0 ? a[a.length - 1] : 50,
                    d = c + 10 * Math.random() - 5;
                d < 0 ? d = 0 : d > 100 && (d = 100), a.push(d)
            }
            for (var e = [], f = 0; f < a.length; ++f) e.push([f, a[f]]);
            return e
        },
        d = [],
        b = 300,
        e = function() {
            for (d.length > 0 && (d = d.slice(1)); d.length < b;) {
                var a = d.length > 0 ? d[d.length - 1] : 50,
                    c = a + 10 * Math.random() - 5;
                c < 0 ? c = 0 : c > 100 && (c = 100), d.push(c)
            }
            for (var e = [], f = 0; f < d.length; ++f) e.push([f, d[f]]);
            return e
        },
        f = 30,
        g = 30;
    g && !isNaN(+g) && (f = +g, f < 1 ? f = 1 : f > 2e3 && (f = 2e3), $(this).val("" + f));
    var h = {
            color: "#F8B98B",
            data: c()
        },
        i = {
            color: "#31CFF9",
            data: e()
        },
        j = $.plot("#multiple-real-timeupdate", [h, i], {
            series: {
                shadowSize: 0,
                lines: {
                    show: true,
                    fill: true
                },
            },
            yaxis: {
                min: 0,
                max: 100
            },
            lines: {
                fill: true,
                lineWidth: 3,
                fillColor: {
                    colors: [{ opacity: 0.5 }, { opacity: 0.5 } ]
                }
            },
            xaxis: {
                show: !1
            },
            grid: {
                borderWidth: 0
            },
            colors: ["#11d89c", "#00baf2"]
        }),
        k = function() {
            j.setData([c(), e()]), j.draw(), setTimeout(k, f)
        };
    k()
}