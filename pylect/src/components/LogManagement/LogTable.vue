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
            <Page :total="logData.length" :current="currentPage" @on-change="handlePageChange" />
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
            logData:[],
            pageSize: 10,
            currentPage: 1,

            // !!!需要补充
            queryParam: {
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
                title: '时间',
                align: "center",
                dataIndex: 'time',
                key: 'time',

            },
            {
                title: '操作',
                align: "center",
                dataIndex: 'operation',
                key: 'operation',
            },
            {
                title: '参数',
                align: "center",
                dataIndex: 'parameter',
                key: 'parameter',
            },
            {
                title: '内容',
                align: "center",
                dataIndex: 'content',
                key: 'content',
                //width: 240,
            },
            ],

            data: [
                {
                    operation: '倒入传感器',
                    content: '{sensor}',
                },
            ],
        }
        },
        computed: {
            // Create a computed property for the data of the current page
            pagedData() {
                const start = (this.currentPage - 1) * this.pageSize;
                const end = start + this.pageSize;
                return this.logData.slice(start, end);
            },

            // Calculate the total number of pages
            totalPages() {
                return Math.ceil(this.logData.length / this.pageSize);
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
                };

                pywebview.api.queryLog(JSON.stringify(params)).then(response => {
                if (response.code === 200) {
                    this.logData = response.result;
                    //console.log("2. this is from", response)
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
