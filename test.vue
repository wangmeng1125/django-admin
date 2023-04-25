<template>
    <div class="chart-container">
        <div ref="chart" class="chart"> </div>
    </div>
</template>

<script>
    import * as echarts from "echarts";

    export default {
        name: 'data_target',
        data() {
            return  {
                chartInstance: null,
                ValidityState: [],
                test: [],
                GFLOPs_512: []
            }
        },
        mounted() {
            const chartDom = this.$refs.chart
            const myChart = echarts.init(chartDom)

            for (let i = 0; i < 12; i++) {
                this.ValidityState.push(Math.random() * 100)
                this.test.push(Math.random() * 100)
                this.chartInstance.push(Math.random() * 100)
                this.GFLOPs_512.push(Math.random() * 100)
            }

            const option = {
                xAxis: {
                    type: 'category',
                    data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                },
                yAxis: {
                    type: 'value',
                    max: 100
                },
                series: [
                    
                        {
                            name: 'Validation_mIoU',
                            type: 'line',
                            data: this.Validation_mIoU
                         },
                        {
                            name: 'Test_Score',
                            type: 'line',
                            data: this.Test_Score
                        },
                        {
                            name: 'params_M',
                            type: 'line',
                            data: this.params_M
                        },
                        {
                            name: 'GFLOPs_512',
                            type: 'line',
                            data: this.GFLOPs_512
                        }
                ]

            }
            myChart.setOptions(options)
            this.chartInstance = myChart
        },

        beforeDestroy() {
            const charDom = this.$refs.chart
            echarts.dispose(charDom)
        }

    }
</script>