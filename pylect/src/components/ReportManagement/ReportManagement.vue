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
                      <Table border :columns="columns" :data="taskData"></Table>
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
            taskParam: {
                dateRecord: '',
            },

            columns: [
                {
                type: 'selection',
                align: 'center',
                width: '10%',
                },
                {
                    title: '任务名称',
                    dataIndex: 'taskId',
                    key: 'taskId',
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

            taskData: [
                {

                }
            ],

            
        }
    },

    //刷新pywebview
    beforeCreate() {
            this.isPyWebViewReady = (typeof pywebview !== 'undefined');
        },
    created() {
        if (this.isPyWebViewReady) {
            this.updateTaskList(this.taskParam);
        }
    },
    mounted() {
        if (!this.isPyWebViewReady) {
            window.addEventListener('load', () => {
                this.updateTaskList(this.taskParam);
            });
        }
    },
    methods :{
        searchQuery() {
            this.$refs.uncollapsedTable.fetchReportData(this.queryParam);
            console.log('1 search.',this.queryParam);
        },
        updateTaskList(queryParam) {
            if (typeof pywebview === 'undefined') {
                console.log('pywebview is not yet defined. Retrying in 1 second...');
                setTimeout(() => this.updateTaskList(queryParam), 1000);
                return;
            }
            const params = {
                dateRecord: queryParam ? queryParam.dateRecord : '',
            };
            pywebview.api.queryTask(JSON.stringify(params)).then(response => {
                console.log('3. ',response)
                if (response.code === 200) {
                    this.taskList = response.result.map(task => ({ value: task, label: task }));
                    console.log('4. ',response.result)
                    this.taskData = response.result; // Update the data for the Table
                } else {
                    console.error('Error fetching task list:', response.message);
                }
            });
        },
    }


  }
  </script>