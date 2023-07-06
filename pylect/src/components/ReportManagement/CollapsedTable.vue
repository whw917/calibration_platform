<style scoped>
.table-page{
    width: 80%;
    margin: auto;
}

.page-bar{
    text-align:right;
    margin-top: 20px;
}

</style>

<template>
    <div class="table-page">

        <Row  style="display: flex; justify-content: space-between;" glutter="560"> 
            <Col style="margin-right: 50px;" flex="1">
              <Table border :columns="columns1" :data="data1"></Table>
            </Col>
          
            <Col flex="5">
              <Table border :columns="columns" :data="data"></Table>
            </Col>

            
        </Row>

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
                title: '标定任务名称',
                align: "center",
                dataIndex: 'taskName',
                key: "taskName"
                //width: 240,
            },
            
            {
                title: '设备编号',
                align: "center",
                dataIndex: 'equiNumber',
                //width: 240,
            },
            {
                title: '芯片号',
                align: "center",
                dataIndex: 'equiName',
                //width: 240,
            },
            {
                title: '传感器类型',
                align: "center",
                dataIndex: 'equiType',
                //width: 240,
            },
            {
                title: '标定日期',
                align: "center",
                dataIndex: 'caliTime',
                //width: 240,
            },
            {
                title: '精度',
                align: "center",
                dataIndex: 'precise',
                width: 100,
            },
            {
                title: '结论',
                align: "center",
                dataIndex: 'conclusion',
                width: 100,
            },
            {
                title: '操作',
                align: "center",
                dataIndex: 'operation',
                scopedSlots: { customRender: 'operation' },
                scopedSlots: { customRender: "operation" },
                //width: 240,
            },
            ],

            columns1: [
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

            data1: [
                {

                }
            ],


            data: [
                {
                    taskName: 'New York',
                
                }
            ],
        }
        },
        methods: {
        }

  }
  </script>