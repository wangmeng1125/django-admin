<!--
 * @Description:
 * @Author: wangmeng 
 * @version:
 * @Date: 2022-04-08 12:44:41
 * @LastEditors: hongzai
 * @LastEditTime: 2022-04-08 12:54:31
 <div class="chart-container" ref="chart"></div>

   import echarts from 'echarts'
  export default {
    name: 'data_target',
-->
<template>
  <div class="chart-container">
    <h3>Data Target model view </h3>
    <div ref="chart" class="chart"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'data_target',
  data() {
    return {
      chartInstance: null,
      Validation_mIoU: [],
      Test_Score: [],
      params_M: [],
      GFLOPs_512: []
    }
  },
  mounted() {
    // 获取 DOM 节点
    const chartDom = this.$refs.chart
    // 初始化 Echarts 实例
    const myChart = echarts.init(chartDom)

    // 生成随机数据
    for (let i = 0; i < 12; i++) {
      this.Validation_mIoU.push(Math.random() * 100)
      this.Test_Score.push(Math.random() * 100)
      this.params_M.push(Math.random() * 100)
      this.GFLOPs_512.push(Math.random() * 100)
    }

    // 定义图表配置项和数据
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
    // 使用刚刚定义的配置项和数据显示图表
    myChart.setOption(option)

    // 保存图表实例
    this.chartInstance = myChart
  },
  beforeDestroy() {
    // 获取 DOM 节点
    const chartDom = this.$refs.chart
    // 销毁 Echarts 实例
    echarts.dispose(chartDom)
  },
  methods: {}
}
</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 500px;
}
.chart {
  width: 100%;
  height: 100%;
}
</style>

