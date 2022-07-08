( function ( $ ) {
    "use strict";

    //Team chart
    var ctx = document.getElementById( "team-chart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "05/2021", "06/2021", "07/2021", "08/2021", "09/2021", "10/2021", "11/2021", "12/2021", "01/2022", "02/2022", "03/2022", "04/2022" ],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [ {
                data: [ 79, 81, 76, 79, 78, 77, 79, 78, 76, 78, 78, 77 ],
                label: "OEE",
                backgroundColor: 'rgba(0,200,155,.35)',
                borderColor: 'rgba(0,200,155,0.60)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(0,200,155,0.60)',
                },{
                data: [ 70, 90, 46, 39, 38, 47, 69, 38, 46, 38, 38, 47 ],
                label: "Eficiencia",
                backgroundColor: 'rgba(0,194,146,.25)',
                borderColor: 'rgba(0,194,146,0.5)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(0,194,146,0.5)',
                },{
                data: [ 25, 45, 16, 59, 95, 90, 80, 94, 91, 86, 87, 71 ],
                label: "Calidad",
                backgroundColor: 'rgba(160,167,79,.45)',
                borderColor: 'rgba(160,167,79,0.75)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(160,167,79,0.75)',
                    } ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
            },
            legend: {
                display: false,
                position: 'top',
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                },


            },
            scales: {
                xAxes: [ {
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Month'
                    }
                        } ],
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                        } ]
            },
            title: {
                display: false,
            }
        }
    } );


    //Sales chart
    var ctx = document.getElementById( "sales-chart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "05/2021", "06/2021", "07/2021", "08/2021", "09/2021", "10/2021", "11/2021", "12/2021", "01/2022", "02/2022", "03/2022", "04/2022" ],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [ {
                label: "OEE",
                data: [ 79, 81, 76, 79, 78, 77, 79, 78, 76, 78, 78, 77 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(220,53,69,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(220,53,69,0.75)',
                    }, {
                label: "Eficiencia",
                data: [ 70, 90, 46, 39, 38, 47, 69, 38, 46, 38, 38, 47 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(40,167,69,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(40,167,69,0.75)',
                    }, {
                label: "Calidad",
                data: [ 25, 45, 16, 59, 95, 90, 80, 94, 91, 86, 87, 71 ],
                backgroundColor: 'transparent',
                borderColor: 'rgba(160,167,79,0.75)',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(160,167,79,0.75)',
                    } ]
        },
        options: {
            responsive: true,

            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
            },
            legend: {
                display: false,
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                },
            },
            scales: {
                xAxes: [ {
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Month'
                    }
                        } ],
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                        } ]
            },
            title: {
                display: false,
                text: 'Normal Legend'
            }
        }
    } );







    //line chart
    var ctx = document.getElementById( "lineChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "05/2021", "06/2021", "07/2021", "08/2021", "09/2021", "10/2021", "11/2021", "12/2021", "01/2022", "02/2022", "03/2022", "04/2022" ],
            datasets: [
                {
                    label: "OEE",
                    borderColor: "rgba(0,0,0,.09)",
                    borderWidth: "1",
                    backgroundColor: "rgba(0,0,0,.07)",
                    data: [ 79, 81, 76, 79, 78, 77, 79, 78, 76, 78, 78, 77 ]
                            },
                {
                    label: "Eficiencia",
                    borderColor: "rgba(0, 194, 146, 0.9)",
                    borderWidth: "1",
                    backgroundColor: "rgba(0, 194, 146, 0.5)",
                    pointHighlightStroke: "rgba(26,179,148,1)",
                    data: [ 70, 90, 46, 39, 38, 47, 69, 38, 46, 38, 38, 47 ]
                            },
                {
                    label: "Calidad",
                    borderColor: "rgba(0, 194, 146, 0.9)",
                    borderWidth: "1",
                    backgroundColor: "rgba(0, 194, 146, 0.5)",
                    pointHighlightStroke: "rgba(26,179,148,1)",
                    data: [ 25, 45, 16, 59, 95, 90, 80, 94, 91, 86, 87, 71 ]
                            }
                        ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                intersect: false
            },
            hover: {
                mode: 'nearest',
                intersect: true
            }

        }
    } );


    //bar chart
    var ctx = document.getElementById( "barChart" );
    //    ctx.height = 200;
    var myChart = new Chart( ctx, {
        type: 'bar',
        data: {
            labels: [ "05/2021", "06/2021", "07/2021", "08/2021", "09/2021", "10/2021", "11/2021", "12/2021", "01/2022", "02/2022", "03/2022", "04/2022" ],
            datasets: [
                {
                    label: "OEE",
                    data: [ 79, 81, 76, 79, 78, 77, 79, 78, 76, 78, 78, 77 ],
                    borderColor: "rgba(0, 194, 146, 0.9)",
                    borderWidth: "0",
                    backgroundColor: "rgba(0, 194, 146, 0.5)"
                            },
                {
                    label: "Eficiencia",
                    data: [ 70, 90, 46, 39, 38, 47, 69, 38, 46, 38, 38, 47 ],
                    borderColor: "rgba(0,0,0,0.09)",
                    borderWidth: "0",
                    backgroundColor: "rgba(0,0,0,0.07)"
                            },
                {
                    label: "Calidad",
                    data: [ 25, 45, 16, 59, 95, 90, 80, 94, 91, 86, 87, 71 ],
                    borderColor: "rgba(0, 194, 146, 0.9)",
                    borderWidth: "0",
                    backgroundColor: "rgba(0,167,79,0.75)"
                            }
                        ]
        },
        options: {
            scales: {
                yAxes: [ {
                    ticks: {
                        beginAtZero: true
                    }
                                } ]
            }
        }
    } );

    //radar chart
    var ctx = document.getElementById( "radarChart" );
    ctx.height = 160;
    var myChart = new Chart( ctx, {
        type: 'radar',
        data: {
            labels: [ [ "10/2021" ], [ "11/2021" ], "12/2021", [ "01/2022" ], "02/2022", "03/2022", "04/2022" ],
            datasets: [
                {
                    label: "OEE",
                    data: [ 77, 79, 78, 76, 78, 78, 77 ],
                    borderColor: "rgba(0, 194, 146, 0.6)",
                    borderWidth: "1",
                    backgroundColor: "rgba(0, 194, 146, 0.4)"
                            },
                {
                    label: "Eficiencia",
                    data: [ 47, 69, 38, 46, 38, 38, 47 ],
                    borderColor: "rgba(0, 194, 146, 0.7",
                    borderWidth: "1",
                    backgroundColor: "rgba(0, 194, 146, 0.5)"
                            }
                        ]
        },
        options: {
            legend: {
                position: 'top'
            },
            scale: {
                ticks: {
                    beginAtZero: true
                }
            }
        }
    });


    //pie chart
    var ctx = document.getElementById( "pieChart" );
    ctx.height = 300;
    var myChart = new Chart( ctx, {
        type: 'pie',
        data: {
            datasets: [ {
                data: [ 53, 41, 6, 0 ],
                backgroundColor: [
                                    "rgba(0, 194, 146,0.9)",
                                    "rgba(0, 194, 146,0.7)",
                                    "rgba(0, 194, 146,0.5)",
                                    "rgba(0,0,0,0.07)"
                                ],
                hoverBackgroundColor: [
                                    "rgba(0, 194, 146,0.9)",
                                    "rgba(0, 194, 146,0.7)",
                                    "rgba(0, 194, 146,0.5)",
                                    "rgba(0,0,0,0.07)"
                                ]

                            } ],
            labels: [
                            "Cambio de molde",
                            "Maquina/Periferico",
                            "Problemas en el molde"
                        ]
        },
        options: {
            responsive: true
        }
    } );

    //doughut chart
    var ctx = document.getElementById( "doughutChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'doughnut',
        data: {
            datasets: [ {
                data: [ 53, 41, 6, 0 ],
                backgroundColor: [
                                    "rgba(0, 194, 146,0.9)",
                                    "rgba(0, 194, 146,0.7)",
                                    "rgba(0, 194, 146,0.5)",
                                    "rgba(0,0,0,0.07)"
                                ],
                hoverBackgroundColor: [
                                    "rgba(0, 194, 146,0.9)",
                                    "rgba(0, 194, 146,0.7)",
                                    "rgba(0, 194, 146,0.5)",
                                    "rgba(0,0,0,0.07)"
                                ]

                            } ],
            labels: [
                            "Cambio de molde",
                            "Maquina/Periferico",
                            "Problemas en el molde"
                        ]
        },
        options: {
            responsive: true
        }
    } );

    //polar chart
    var ctx = document.getElementById( "polarChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'polarArea',
        data: {
            datasets: [ {
                data: [ 53, 41, 6, 0 ],
                backgroundColor: [
                                    "rgba(0, 194, 146,0.9)",
                                    "rgba(0, 194, 146,0.8)",
                                    "rgba(0, 194, 146,0.7)",
                                    "rgba(0,0,0,0.2)",
                                    "rgba(0, 194, 146,0.5)"
                                ]

                            } ],
            labels: [
                            "Cambio de molde",
                            "Maquina/Periferico",
                            "Problemas en el molde"
                        ]
        },
        options: {
            responsive: true
        }
    } );

    // single bar chart
    var ctx = document.getElementById( "singelBarChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'bar',
        data: {
            labels: [ "05/2021", "06/2021", "07/2021", "08/2021", "09/2021", "10/2021", "11/2021", "12/2021", "01/2022", "02/2022", "03/2022", "04/2022" ],
            datasets: [
                {
                    label: "OEE",
                    data: [ 79, 81, 76, 79, 78, 77, 79, 78, 76, 78, 78, 77 ],
                    borderColor: "rgba(0, 194, 146, 0.9)",
                    borderWidth: "0",
                    backgroundColor: "rgba(0, 194, 146, 0.5)"
                            }
                        ]
        },
        options: {
            scales: {
                yAxes: [ {
                    ticks: {
                        beginAtZero: true
                    }
                                } ]
            }
        }
    } );
} )
( jQuery );