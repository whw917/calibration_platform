<template>
  <div ref="chart" class="lineChart" label="测量者"></div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.chart = echarts.init(this.$refs.chart)
    this.chart.setOption({
      tooltip: {
        trigger: 'axis'
      },
      legend: {
        data: [
          //{ name: '土壤含水量', icon: 'circle' },
          
        ],
        itemWidth: 6,
        itemHeight: 6,
        itemGap: 30,
        textStyle: {
          color: '#333',
          fontSize: 20,
          lineHight: 20
        }
      },
      xAxis: [
        {
          type: 'category',
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            onZero: false,
            lineStyle: {
              color: '#333'
            }
          },
          data: ['2020/11/24 09:56:23', '2020/11/25 09:56:23', '2020/11/26 09:56:23', '2020/11/27 09:56:23']
        }
      ],
      yAxis: [
        {
          type: 'value',
          axisLabel: {
            textStyle: {
              color: '#333',
              fontSize:8
            }
          }
        }
      ],
      series: [
        {
          name: '土壤含水量',
          type: 'line',
          smooth: true,
          data: [320, 332, 301, 334]
        },
        {
          name: '土壤温度',
          type: 'line',
          smooth: true,
          data: [120, 132, 101, 134]
        },
        {
          name: '土壤电导率',
          type: 'line',
          smooth: true,
          data: [862, 1018, 964, 1026],
          markLine: {
            lineStyle: {
              type: 'dashed'
            },
            data: [
              [{ type: 'min' }, { type: 'max' }]
            ]
          }
        }
      ]
    })
  }
}
</script>

<style scoped>
.lineChart{
  width: 400mm;
  height: 70mm;
  margin: auto;
}
</style>
