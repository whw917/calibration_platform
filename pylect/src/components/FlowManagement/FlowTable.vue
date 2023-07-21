<style scoped>


.page-bar{
    text-align:right;
    margin-top: 20px;
}

</style>

<template>
    <div >
            <Table border :columns="columns" :data="flowData">
                <template v-slot:operation="{ row }"> 

                    <a @click="edit(row)" >编辑</a>
                    <Divider type="vertical" />
                    <a @click="deleteRow(row)" >删除</a>

                </template>
            </Table>

        <div class="page-bar">
            <Page :total="100" />
        </div>

    </div>
</template>
  
  <script>
  import { Row, Input, Button, Table, Page, Space, FormItem, resolveComponent} from 'view-design'
  
  
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
            flowData: [],

            queryParam: {
                keyword: '',
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
                fixed: "left",
            },
            {
                title: '流程名称',
                align: "center",
                dataIndex: 'flow_name',
                key: 'flow_name',
                fixed: "left",
                width: 160,
            },
            {
                title: '流程类型',
                align: "center",
                dataIndex: 'flow_type',
                key: 'flow_type',
                fixed: "left",
                width: 100,
            },
            {
                title: '驱动协议',
                align: "center",
                dataIndex: 'driver',
                key: 'driver',
                width: 180,
            },
            {
                title: '传感器协议',
                align: "center",
                dataIndex: 'sensor_protocol',
                key: "sensor_protocol",
                width: 180,
            },
            {
                title: '设备名称',
                align: "center",
                dataIndex: 'device_name',
                key: 'device_name',
                width: 180,
            },
            {
                title: '设备协议',
                align: "center",
                dataIndex: 'device_protocol',
                key: 'device_protocol',
                width: 160,
            },
            {
                title: '运动时间(s)',
                align: "center",
                dataIndex: 'move_seconds',
                key: 'move_seconds',
                width: 120,
            },
            {
                title: '读秒延迟(s)',
                align: "center",
                dataIndex: 'wait_seconds',
                key: 'wait_seconds',
                width: 120,
            },
            {
                title: '读数次数',
                align: "center",
                dataIndex: 'read_times',
                key: 'read_times',
                width: 120,
            },
            {
                title: '平台精度',
                align: "center",
                dataIndex: 'precise',
                key: 'precise',
                width: 120,
            },
            {
                title: '传感器轴数',
                align: "center",
                dataIndex: 'sensor_sum',
                key: 'sensor_sum',
                width: 120,
            },
            {
                title: '传感器名称',
                align: "center",
                dataIndex: 'sensor_name',
                key: 'sensor_name',
                width: 160,
            },
            {
                title: '点数列表',
                align: "center",
                dataIndex: 'scale_list',
                key: 'scale_list',
                width: 160,
            },
            {
                title: '操作',
                align: "center",
                dataIndex: 'operation',
                fixed: 'right',
                slot: 'operation',
                width: 150,
            },
            
            ],

            data: [
                {
                    flow_type: '查询',
                    device_protocol: 1,
                    wait_seconds: 10,
                    move_seconds: 4, 
                },
            ],
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
                keyword: queryParam ? queryParam.keyword : '',
                column: 'time',  // Sort by time, for example
                orderby: 'desc',  // In descending order, for example
            };

            console.log("1. this is from the tabel", queryParam)
            pywebview.api.queryFlow(JSON.stringify(params)).then(response => {
            if (response.code === 200) {
                this.flowData = response.result;
                this.$emit('data-fetched', this.flowData); 
            } else {
                console.error('Error fetching flow data:', response.message);
            }
            });
        },
        edit(row) {
            const id = row.id; 
            console.log("id is: ", id)
            this.$router.push({ name: 'EditFlow', params: { id: row.id } });
            
        },

        deleteRow(row) {
            console.log('preparing to delete row', row)
            this.$Modal.confirm({
                title: 'Confirm Deletion',
                content: 'Are you sure you want to delete this flow?',
                onOk: () => {
                    pywebview.api.deleteFlow(row.id).then(response => {
                        if (response.code === 200) {
                            console.log('Flow data deleted successfully.');
                            this.fetchFlowData(this.queryParam); // fetch the data again after deletion
                        } else {
                            console.error('Error deleting flow data:', response.message);
                        }
                    });
                },
            });
        },


    }

  }
  </script>