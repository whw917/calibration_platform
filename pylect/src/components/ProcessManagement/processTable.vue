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
                dataIndex: 'processName',
                key: 'processName',
                fixed: "left",
                width: 160,
            },
            {
                title: '流程类型',
                align: "center",
                dataIndex: 'processType',
                key: 'processType',
                fixed: "left",
                width: 100,
            },
            {
                title: '驱动协议',
                align: "center",
                dataIndex: 'driveCont',
                key: 'driveCont',
                width: 160,
            },
            {
                title: '传感器协议',
                align: "center",
                dataIndex: 'equiCont',
                key: "equiCont",
                width: 160,
            },
            {
                title: '设备名称',
                align: "center",
                dataIndex: 'equiName',
                key: 'equiName',
                width: 160,
            },
            {
                title: '设备协议',
                align: "center",
                dataIndex: 'equiCont',
                key: 'equiCont',
                width: 160,
            },
            {
                title: '运动时间(s)',
                align: "center",
                dataIndex: 'actionTime',
                key: 'actionTime',
                width: 120,
            },
            {
                title: '读秒延迟(s)',
                align: "center",
                dataIndex: 'delayTime',
                key: 'delayTime',
                width: 120,
            },
            {
                title: '读数次数',
                align: "center",
                dataIndex: 'actionTime',
                key: 'actionTime',
                width: 120,
            },
            {
                title: '平台精度',
                align: "center",
                dataIndex: 'accuracy',
                key: 'accuracy',
                width: 120,
            },
            {
                title: '传感器轴数',
                align: "center",
                dataIndex: 'equiNumber',
                key: 'equiNumber',
                width: 120,
            },
            {
                title: '传感器名称',
                align: "center",
                dataIndex: 'equiName',
                key: 'equiName',
                width: 160,
            },
            {
                title: '点数列表',
                align: "center",
                dataIndex: 'pointList',
                key: 'pointList',
                width: 160,
            },
            {
                title: '操作',
                align: "center",
                dataIndex: 'operation',
                fixed: 'right',
                //slot: 'action'  // Here we define a slot named 'action'
                width: 160,
            },
            
            ],

            data: [
                {
                    processType: '查询',
                    equiCont: 1,
                    delayTime: 10,
                    actionTime: 4, 
                },
            ],
        }
        },
        methods: {
        }

  }
  </script>