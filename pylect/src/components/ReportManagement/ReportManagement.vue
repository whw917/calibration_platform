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
        <h2 class="title">标定报告管理</h2>

        <Form class="search-form" ref="formRef" :model="queryParam"  >
            <Row class="search-bar" glutter="16">
                <!-- 时间查询 -->
                <Col span="6" align="left">
                    <FormItem label="选择时间:" > 
                        <DatePicker v-model="queryParam.dateRecord" type="daterange" placement="bottom-end" placeholder="Select date" style="width: 70%" />
                    </FormItem>
                </Col>
                <!-- 任务名称，设备编号或芯片号 模糊查询 -->
                <Col span="5" align="left">
                    <FormItem >
                    <Input search v-model="queryParam.keyword" placeholder="请输入任务名称，设备编号或芯片号" style="width: 90%" />
                    </FormItem>
                </Col>

                <!-- 下滑列表选择 -->
                <Col span="2" align="left">
                    <FormItem >
                        <Select  style="width:80%">
                            <Option v-model="queryParam.result" v-for="item in choicelist" :value="item.value" :key="item.value">{{ item.label }}</Option>
                        </Select>
                    </FormItem>
                </Col>

                <!-- 查询按钮 -->
                <Col span="2" align="left">
                    <Button type="primary" @click="searchQuery" icon="search">查询</Button>
                </Col>

                <!-- 选择合并 -->
                <Col span="3" align="left">
                    <Checkbox v-model="isCollapse">合并同一个设备报告</Checkbox>
                </Col>

                <Col span="4" align="right">
                    <Button type="primary">导出</Button>
                </Col>
            </Row>

            <div class="table-page">

                <Row  style="display: flex; justify-content: space-between;" glutter="32"> 
                    <Col  flex="1">
                      <Table border :columns="columns" :data="data"></Table>
                    </Col>
                  
                    <Col flex="7"> 
                        
                        <UncollapsedTable ref="uncollapsedTable" v-if="!isCollapse" />
                        <CollapsedTable ref="collapsedTable" v-else />

                    </Col>
                </Row>
            </div>   
            
        </Form>
  
    </div>
  </template>
  
  <script>
  import { Input, Button, Table, Page, Space, model, FormItem, Collapse} from 'view-design'
  import CollapsedTable from './CollapsedTable.vue'
  import UncollapsedTable from './UncollapsedTable.vue'

  export default {
    components: {
      Input,
      Button,
      Table,
      Page,
      FormItem,

      CollapsedTable,
      UncollapsedTable,

    },
    data() {
        return {
            isCollapse: false,
            queryParam: {
                dateRecord: '',
                keyword: '',
                result: '',
                taskId: '',
                reporttype: 'prod',
            },

            columns: [
                {
                type: 'selection',
                align: 'center',
                width: '10%',
                },
                {
                    title: '任务名称',
                    dataIndex: 'taskName',
                    align:"center",
                },
            ],

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

            data: [
                {

                }
            ],

            
        }
    },

    

    methods :{
        searchQuery() {
            this.$refs.uncollapsedTable.fetchReportData(this.queryParam);
            console.log('1 search.',this.queryParam);
        },
    }

  }
  </script>