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
                title: '参数名称',
                align: "center",
                dataIndex: 'paraName',
                key: 'paraName',

            },
            {
                title: '参考值',
                align: "center",
                dataIndex: 'referValue',
                key: 'referValue',
            },
            {
                title: '单位',
                align: "center",
                dataIndex: 'unit',
                key: 'unit',
            },
            {
                title: '说明',
                align: "center",
                dataIndex: 'content',
                key: 'content',
                //width: 240,
            },
            ],

            data: [
                {
                    paraName: '平台精度',
                    unit: '度',
                    content: '{sensor}',
                },
            ],
        }
        },
        methods: {
        }

  }
  </script>