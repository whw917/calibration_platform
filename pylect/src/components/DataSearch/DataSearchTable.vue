<style scoped>


.page-bar{
    text-align:right;
    margin-top: 20px;
}

</style>

<template>
    <div >
    
        <Table border :columns="columns" :data="pagedData">
        </Table>

        <div class="page-bar">
            <Page :total="searchData.length" :current="currentPage" @on-change="handlePageChange" />
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
            searchData:[],
            pageSize: 10,
            currentPage: 1,

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
            columns: [
            {
                title: '序号',
                dataIndex: 'index',
                key:'rowIndex',
                width:80,
                align:"center",
                type: "index",
            },
            {
                title: '传感器SN',
                align: "center",
                dataIndex: 'deviceCode',
                key: "deviceCode"
                //width: 240,
            },
            
            {
                title: '端口',
                align: "center",
                dataIndex: 'port',
                key: 'port',
                //width: 240,
            },
            {
                title: '地址',
                align: "center",
                dataIndex: 'address',
                width: 100,
                key: 'address',
            },
            {
                title: '传感器类型',
                align: "center",
                dataIndex: 'sensorType',
                key: 'sensorType',
                //width: 240,
            },
            {
                title: '通道',
                align: "center",
                dataIndex: 'channel',
                key: 'channel',
                width: 100,
            },
            {
                title: '标定时间',
                align: "center",
                dataIndex: 'time',
                key: 'time',

            },
            {
                title: '测量值',
                align: "center",
                dataIndex: 'measure_Value',
                key: 'measure_Value',
                width: 100,
            },
            {
                title: 'AD值',
                align: "center",
                dataIndex: 'AD_Value',
                key: 'AD_Value',
            },
            {
                title: '参考值',
                align: "center",
                dataIndex: 'refer_Value',
                key: 'refer_Value',
                width: 100,
            },
            {
                title: '流程名称',
                align: "center",
                dataIndex: 'process_Name',
                key: 'process_Name',
                //width: 240,
            },
            {
                title: '任务名称',
                align: "center",
                dataIndex: 'taskId',
                key: 'taskId',
                //width: 240,
            },
            {
                title: '操作员',
                align: "center",
                dataIndex: 'stuff',
                key: 'stuff',
                //width: 240,
            },
            ],
            data: [
                {
                    sensorType: '35',
                    port: 1,
                    measureValue: 3,
                },
            ],
        }
        },

        computed: {
            // Create a computed property for the data of the current page
            pagedData() {
                const start = (this.currentPage - 1) * this.pageSize;
                const end = start + this.pageSize;
                return this.searchData.slice(start, end);
            },

            // Calculate the total number of pages
            totalPages() {
                return Math.ceil(this.searchData.length / this.pageSize);
            }
        },
        //刷新pywebview
        beforeCreate() {
            this.isPyWebViewReady = (typeof pywebview !== 'undefined');
        },
        created() {
            if (this.isPyWebViewReady) {
                this.fetchFlowData(this.queryParam);
            }
        },
        mounted() {
            if (!this.isPyWebViewReady) {
                window.addEventListener('load', () => {
                    this.fetchFlowData(this.queryParam);
                });
            }
        },

        methods: {
            fetchFlowData(queryParam) {
                //console.log("this is from the tabel", queryParam)
                if (typeof pywebview === 'undefined') {
                    console.log('pywebview is not yet defined. Retrying in 1 second...');
                    setTimeout(() => this.fetchFlowData(queryParam), 10);
                    return;
                }
                const params = {
                    deviceCode: queryParam ? queryParam.deviceCode : '',
                    dateRecord: queryParam ? queryParam.dateRecord : '',
                    taskId: queryParam ? queryParam.taskId : '',
                    calcType: queryParam ? queryParam.calcType : '',
                    page: 1,
                    pageSize:10,
                    column: 'time',
                    orderBy: 'desc',
                };

                console.log("1. this is from the tabel", params)
                pywebview.api.queryData(JSON.stringify(params)).then(response => {
                if (response.code === 200) {
                    this.searchData = response.result;
                    console.log("2. this is from", response)
                } else {
                    console.error('Error fetching flow data:', response.message);
                }
                });
            },
            handlePageChange(page) {
                this.currentPage = page;
            },

        }

  }
  </script>