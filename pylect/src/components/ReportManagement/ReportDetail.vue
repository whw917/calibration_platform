<style scoped>

.title {
    font-size: 1em;
    text-align: left;
    margin-bottom: 20px;
    margin-left: 5px;
  }

.search-bar{
    width: 80%;
    margin: auto;
}

.table-page{
    width: 80%;
    margin: auto;
}

</style>

<template>
    <div>
      <h2 class="title">传感器数据详情</h2>
      <div v-if="rowData">
        
        <!-- Other fields... -->
      </div>

      <Form class="search-form" ref="formRef" :model="queryParam"  >
        <Row class="search-bar" glutter="16">
            <!-- 时间查询 -->
            <Col span="6" align="left">
                <p><strong>设备名称:</strong> {{ rowData.taskName }}</p>
                <p><strong>设备编号:</strong> {{ rowData.equiNumber }}</p>
            </Col>


            <!-- 下滑列表选择 -->
            <Col span="7" align="left">
                <FormItem >
                    <Select  label='传感器列表' style="width:80%">
                        <Option v-for="item in equiList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                    </Select>
                </FormItem>
            </Col>


            <Col span="6" align="right">
                <p><strong>标定任务名称:</strong></p>
                <p><strong>标定流程名称:</strong></p>
                <p><strong>标定时间:</strong></p>
            </Col>
        </Row>

        <div class="table-page">

            <Row  style="display: flex; justify-content: space-between;" glutter="32"> 
                <Col  flex="1">
                  <!-- <Table border :columns="columns" :data="data"></Table> !-->
                  <LineChart/>
                </Col>
              
                <Col flex="6"> 
                    <!-- <Table border /> !-->

                </Col>
            </Row>
        </div>   
        
     </Form>



    </div>
  </template>
  
  <script>
  import { Input, Button, Table, Page, Space, model, FormItem} from 'view-design'
  import LineChart from './LineChart.vue'
  
  export default {
    
  

    
    props: ['rowData'],
    created() {
        console.log(this.rowData); // Logs the data passed from the table component
    },

    components: {
      Input,
      Button,
      Table,
      Page,
      FormItem,

      LineChart,
    },

    data() {
        return {
            isCollapse: false,
            queryParam: {
                
            },

            columns: [
                
            ],
 
            data: [
                
            ],

            equiList: [
                    {
                        value: 'equiX',
                        label: '传感器X'
                    },
                    {
                        value: 'equiY',
                        label: '传感器Y'
                    },
                    {
                        value: 'equiZ',
                        label: '传感器Z'
                    }
                ],
        }
    },
    methods :{
        searchQuery(){

        },
    },

  
  
}
  </script>
  