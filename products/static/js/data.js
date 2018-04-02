


$.getJSON('/products/statistics/chartdata', function calldata(d){
    
        var count0_10 = [d.count0_10];
        var count11_20 = [d.count11_20];
        var count21_30 = [d.count21_30];
        console.log(count0_10);
        console.log(count11_20);
        console.log(count21_30);

        $('#chartdesc').text('So we have ' + count0_10 + ' products with total rating between 0 and 10, ' + count11_20 + ' products with total rating between 11 and 20, and ' +  count21_30 + ' products with total rating between 21 and 30')

        var ctx = document.getElementById("myChart");
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                datasets: [{
                    label: 'Total rating between 0 and 10',
                    data: count0_10,
                    backgroundColor: [
                        'rgba(66, 134, 244, 0.6)',
                    ],
                    borderColor: [
                        'rgb(65, 83, 244)',
                    ],
                    borderWidth: 1
                },
                {
                    label: 'Total rating between 11 and 20',
                    data: count11_20,
                    backgroundColor: [
                        'rgba(13, 198, 35, 0.6)',
                    ],
                    borderColor: [
                        'rgb(8, 145, 24)',
                    ],
                    borderWidth: 1
                },
                {
                    label: 'Total rating between 21 and 30',
                    data: count21_30,
                    backgroundColor: [
                        'rgba(214, 38, 199, 0.6)'
                    ],
                    borderColor: [
                        'rgb(163, 29, 151)',
                    ],labels: ["Red"],
                    borderWidth: 1
                }
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                },

                responsive:true
            }
        });
    });

