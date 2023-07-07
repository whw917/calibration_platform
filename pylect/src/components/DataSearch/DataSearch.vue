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
        <h2 class="title">数据查询</h2>

        <Form class="search-form" ref="formRef" :model="queryParam"  >
            <Row class="search-bar" glutter="16">
                <!-- 时间查询 -->
                <Col span="6" align="left">
                    <FormItem label="选择时间:" > 
                        <DatePicker v-model="queryParam.dateRecord" type="daterange" placement="bottom-end" placeholder="Select date" style="width: 70%" />
                    </FormItem>
                </Col>

                
                <!-- 标定任务下滑列表 -->
                <Col span="5" align="left">
                    <FormItem label="任务列表:">
                        <Select  style="width:70%">
                            <Option v-model="queryParam.taskRecord" v-for="item in taskList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                        </Select>
                    </FormItem>
                </Col>

                <!-- 参考值下滑列表 -->
                <Col span="3" align="left">
                    <FormItem >
                        <Select  style="width:70%">
                            <Option v-model="queryParam.valueRecord" v-for="item in valueList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                        </Select>
                    </FormItem>
                </Col>


                <Col align="right">
                    <Button type="primary" @click="searchQuery" icon="search">查询</Button>
                    <Button type="primary">导出</Button>
                </Col>

            </Row>

            <div class="table-page">
                <DataSearchTable/>
            </div>   

        </Form>
  
    </div>
  </template>
  
  <script>
  import { Input, Button, Table, Page, Space, model, FormItem} from 'view-design'
  import DataSearchTable from './DataSearchTable.vue'

  export default {
    components: {
      Input,
      Button,
      Table,
      Page,
      FormItem,

      DataSearchTable,

    },
    data() {
        return {
            isCollapse: false,
            queryParam: {
                dateRecord: '',
                taskRecord: '',
                valueRecord: '',
            },

            taskList: [
                    {
                        value: 'task1',
                        label: '任务1'
                    },
                    {
                        value: 'task2',
                        label: '任务2'
                    },
                    {
                        value: 'task3',
                        label: '任务3'
                    }
            ],

            valueList: [
                    {
                        value: 'averageValue',
                        label: '平均值'
                    },
                    {
                        value: 'collectValue',
                        label: '采集值'
                    },
            ],
        }
    },
    methods :{
        searchQuery(){

        },
    }

  }
  </script>