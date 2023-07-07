<style scoped>


.page-bar{
    text-align:right;
    margin-top: 20px;
}

</style>

<template>
    <div >
    
            <Table border :columns="columns" :data="data">
            </Table>

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
                dataIndex: 'SNumber',
                key: "SNNumber"
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
                dataIndex: 'equiType',
                key: 'equiType',
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
                dataIndex: 'measureValue',
                key: 'measureValue',
                width: 100,
            },
            {
                title: 'AD值',
                align: "center",
                dataIndex: 'ADValue',
                key: 'ADValue',
            },
            {
                title: '参考值',
                align: "center",
                dataIndex: 'referValue',
                key: 'referValue',
                width: 100,
            },
            {
                title: '流程名称',
                align: "center",
                dataIndex: 'processName',
                key: 'processName',
                //width: 240,
            },
            ],

            data: [
                {
                    equiType: '35',
                    port: 1,
                    measureValue: 3,
                },
            ],
        }
        },
        methods: {
            edit(row) {
                console.log('Edit operation for', row)
                // handle edit operation here
            },
            remove(row) {
                console.log('Delete operation for', row)
                // handle delete operation here
            }
        }

  }
  </script>