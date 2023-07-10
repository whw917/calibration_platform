<template>
  <div>
    <h2>测量值数据曲线</h2>
    <div ref="chart" class="lineChart"></div>
    <Checkbox v-model="show1">showA</Checkbox>
    <Checkbox v-model="show2">showB</Checkbox>
  </div>
  
</template>

<script>
import * as echarts from 'echarts'

export default {
  data() {
    return {
      show1: false,
      show2: false,
      chart: null,
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
          { name: '测量值', icon: 'circle' },
          { name: '参考值', icon: 'circle' },
          { name: '差距', icon: 'circle' }

        ],
        itemWidth: 6,
        itemHeight: 6,
        itemGap: 30,
        textStyle: {
          color: '#333',
          fontSize: 12,
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
          //data: [-90, -60,-30,0,30,60,90]
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
          name: '测量值',
          type: 'line',
          smooth: true,
          data: [[-90,2],[-70,2],[-60,3],[-40,5],[-30,2],[-10,1],[0,2],[10,2],[30,2],[60,5],[70,4],[90,2],],

          markLine: {
            lineStyle: {
              type: 'dashed'
            },
            data: [
              [{ type: 'min' }, { type: 'max' }]
            ]
          }
        },
        {
          name: '参考值',
          type: 'line',
          smooth: true,
          data: [[-90,1],[-60,2],[-30,5],[0,3],[30,1],[60,2],[90,3],],
        },
        {
          name: '差距',
          type: 'line',
          smooth: true,
          data: [[-90,2],[-60,2],[-30,3],[0,4],[30,1],[60,2],[90,2],],
          
        },
        
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
