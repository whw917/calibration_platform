<style scoped>


.page-bar{
    text-align:right;
    margin-top: 20px;
}

</style>

<template>
    <div class="table-page">

          
        <Col >
            <Table border :columns="columns" :data="data">
                <template v-slot:operation="{ row }"> 

                    <a @click="expand(row)" >详情</a>
                    <Divider type="vertical" />
                    <a @click="preview(row)" >预览报告</a>

                </template>
            </Table>
            
        </Col>


        <div class="page-bar">
            <Page :total="100" />
        </div>

    </div>
</template>
  
  <script>
  import { Row, Input, Button, Table, Page, Space, FormItem } from 'view-design'
  
  export default {
    components: {
    Input,
    Button,
    Table,
    Page,
    Space,
    FormItem,
    Row
},

    data() {
        return {
            columns: [
            {
                type: 'selection',
                width: 60,
                align: 'center'
            },
            {
                title: '序号',
                dataIndex: 'index',
                key:'rowIndex',
                width:70,
                align:"center",
                type: "index",
            },
            {
                title: '标定任务名称',
                align: "center",
                dataIndex: 'taskName',
                key: "taskName",
                width: 140,
            },
            
            {
                title: '设备编号',
                align: "center",
                dataIndex: 'device_code',
                key: 'device_code',
                //width: 240,
            },
            {
                title: '芯片号',
                align: "center",
                dataIndex: 'chip_Num',
                key: 'chip_Num',
                //width: 240,
            },
            {
                title: '传感器类型',
                align: "center",
                dataIndex: 'sensor_Type',
                key: 'sensor_Type',
                //width: 240,
            },
            {
                title: '标定日期',
                align: "center",
                dataIndex: 'date',
                key: 'date',
            },
            {
                title: '精度',
                align: "center",
                dataIndex: 'precise',
                key: 'precise',
                width: 100,
            },
            {
                title: '结论',
                align: "center",
                dataIndex: 'conclusion',
                key: 'conclusion',
                width: 100,
            },
            {
                title: '操作',
                align: "center",
                dataIndex: 'operation',
                key: 'operation',
                slot: 'operation',  // Here we define a slot named 'operation'
                width: 150,
            },
            ],

            


            data: [
                {
                    taskName: 'New York',
                
                }
            ],
        }
        },
        // 刷新 pywebview
        beforeCreate() {
            this.isPyWebViewReady = (typeof pywebview !== 'undefined');
        },
        created() {
            if (this.isPyWebViewReady) {
                this.fetchReportData();
            }
        },
        mounted() {
            if (!this.isPyWebViewReady) {
                window.addEventListener('load', () => {
                    this.fetchReportData();
                });
            }
        },
        methods: {
            expand(row) {
                // Use the $router.push method to navigate
                this.$router.push({ name: 'ReportDetail', params: { rowData: row } });
            },
            preview(row) {
                console.log('preiview operation for', row)
                // handle delete operation here
            },
            fetchReportData() {
                if (typeof pywebview === 'undefined') {
                    console.log('pywebview is not yet defined. Retrying in 1 second...');
                    setTimeout(() => this.fetchReportData(), 1000);
                    return;
                }
                const params = {
                    dateRecord: '',
                    keyword: '',
                    result: '',
                    taskId: '',
                    reporttype: 'prod',
                };
                pywebview.api.queryReport(JSON.stringify(params)).then(response => {
                    console.log('11.',response);
                    if (response.code === 200) {
                        this.data = response.result;
                    } else {
                        console.error('Error fetching report data:', response.message);
                    }
                });
            },
        }
}

  
  </script>