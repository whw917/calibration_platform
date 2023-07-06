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
</style>

<template>
    <div>
        <h2 class="title">标定报告管理</h2>

        <Form class="search-form" ref="formRef" :model="queryParam"  >
            <Row class="search-bar" glutter="16">
                <Col span="6" align="left">
                    <FormItem label="选择时间:" > 
                        <DatePicker type="daterange" placement="bottom-end" placeholder="Select date" style="width: 70%" />
                    </FormItem>
                </Col>

                <Col span="5" align="left">
                    <FormItem >
                    <Input search v-model="queryParam.searchRecord" placeholder="请输入任务名称，设备编号或芯片号" style="width: 90%" />
                    </FormItem>
                </Col>

                <Col span="2" align="left">
                    <FormItem >
                        <Select  style="width:80%">
                            <Option v-for="item in choicelist" :value="item.value" :key="item.value">{{ item.label }}</Option>
                        </Select>
                    </FormItem>
                </Col>


                <Col span="2" align="left">
                    <Button type="primary" @click="searchQuery" icon="search">查询</Button>
                </Col>

                <Col span="3" align="left">
                    <Checkbox v-model="collapse">合并同一个设备报告</Checkbox>
                </Col>

                <Col span="4" align="right">
                    <Button type="primary">导出</Button>
                </Col>
            </Row>

            <CollapsedTable/>


            
            
        </Form>
  
    </div>
  </template>
  
  <script>
  import { Input, Button, Table, Page, Space, model, FormItem, Collapse} from 'view-design'
  import CollapsedTable from './CollapsedTable.vue'

  export default {
    components: {
      Input,
      Button,
      Table,
      Page,
      FormItem,

      CollapsedTable,

    },
    // your data and methods...

    data() {
        return {
            collapse: false,
            queryParam: {
                searchRecord: '',
            },
            choicelist: [
                    {
                        value: 'all',
                        label: '全部'
                    },
                    {
                        value: 'pass',
                        label: '合格'
                    },
                    {
                        value: 'fail',
                        label: '不合格'
                    }
                ],
        }
    },
    methods :{
        searchQuery(){

        },
    }

  }
  </script>