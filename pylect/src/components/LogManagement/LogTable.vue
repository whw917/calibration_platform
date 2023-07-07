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
        methods: {
        }

  }
  </script>