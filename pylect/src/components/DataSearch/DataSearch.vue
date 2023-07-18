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

                <Col span="7" align="left">
                    <FormItem >
                    <Input search v-model="queryParam.deviceCode" placeholder="请输入设备号SN" style="width: 90%" />
                    </FormItem>
                </Col>

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
                            <Option v-model="queryParam.taskId" v-for="item in taskList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                        </Select>
                    </FormItem>
                </Col>

                <!-- 参考值下滑列表 -->
                <Col span="3" align="left">
                    <FormItem >
                        <Select  style="width:70%">
                            <Option v-model="queryParam.calcType" v-for="item in valueList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                        </Select>
                    </FormItem>
                </Col>


                <Col align="right">
                    <Button type="primary" @click="searchQuery" icon="search">查询</Button>
                    <Button type="primary">导出</Button>
                </Col>

            </Row>

            <div class="table-page">
                <DataSearchTable ref="dataSearchTable"/>
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
            queryParam: {
                deviceCode: '',
                dateRecord: '',
                taskId: '',
                calcType: '',
                page: '',
                pageSize: '',
                column: '',
                orderBy: '',
            },
            taskParam: {
                dateRecord: '',
            },
            taskList: [],
            List: [
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

    watch: {
        taskList(newTaskList) {
            // If the new task list is not empty and it doesn't include the current task ID,
            // then update the task ID to the value of the first task in the new list.
            if (newTaskList.length > 0 && !newTaskList.map(task => task.value).includes(this.queryParam.taskId)) {
                this.queryParam.taskId = newTaskList[0].value;
            }
        },
        valueList(newValueList) {
            // If the new value list is not empty and it doesn't include the current calc type,
            // then update the calc type to the value of the first item in the new list.
            if (newValueList.length > 0 && !newValueList.map(value => value.value).includes(this.queryParam.calcType)) {
                this.queryParam.calcType = newValueList[0].value;
            }
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
            this.$refs.dataSearchTable.fetchFlowData(this.queryParam);
            console.log(this.queryParam);
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
            if (response.code === 200) {
                this.taskList = response.result.map(task => ({ value: task, label: task }));
                this.$refs.dataSearchTable.taskList = this.taskList; // Update the prop in child component
            } else {
                console.error('Error fetching task list:', response.message);
            }
        });
        },
    }

  }
  </script>