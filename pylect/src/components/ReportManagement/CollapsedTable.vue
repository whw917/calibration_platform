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
                width:80,
                align:"center",
                type: "index",
            },
            
            {
                title: '设备编号',
                align: "center",
                dataIndex: 'equiNumber',
                key:'equiNumber'
                //width: 240,
            },
            {
                title: '传感器类型',
                align: "center",
                dataIndex: 'equiType',
                key: 'equiType',
                //width: 240,
            },
            {
                title: '标定日期',
                align: "center",
                dataIndex: 'caliTime',
                key: 'caliTime',
                //width: 240,
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
        methods: {
            expand(row) {
                // Use the $router.push method to navigate
                this.$router.push({ name: 'ReportDetail', params: { rowData: row } });
            },
            preview(row) {
                console.log('preiview operation for', row)
                // handle delete operation here
            }
        }

  }
  </script>