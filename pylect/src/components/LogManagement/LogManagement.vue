<style scoped>

.title {
    font-size: 1em;
    text-align: left;
    margin-bottom: 20px;
    margin-left: 5px;
  }


.search-bar{
    width: 80%;
    margin: auto;
}

.table-page{
    width: 80%;
    margin: auto;
}
</style>

<template>
    <div>
        <h2 class="title">日志管理</h2>

        <Form class="search-form" ref="formRef" :model="queryParam"  >
            <Row class="search-bar" glutter="16">
                <!-- 查询 -->
                <Col span="7" align="left">
                    <FormItem >
                    <Input search v-model="queryParam.searchRecord" placeholder="请输入" style="width: 90%" />
                    </FormItem>
                </Col>

        
                <Col>
                    <Button type="primary" @click="searchQuery" icon="search">查询</Button>
                </Col>

                <Col align="right" offset="8">
                    <Button type="primary" @click="clear" icon="search">清空</Button>
                    <Button type="primary" @click="exportTemp" icon="search">导出</Button>
                </Col>

            </Row>

            <div class="table-page">
                <LogTable/>
            </div>   

        </Form>
  
    </div>
  </template>
  
  <script>
  import { Input, Button, Table, Page, Space, model, FormItem} from 'view-design'
  import LogTable from './LogTable.vue'

  export default {
    components: {
      Input,
      Button,
      Table,
      Page,
      FormItem,

      LogTable,

    },
    data() {
        return {
            isCollapse: false,
            queryParam: {
                searchRecord: '',
            },
        }
    },
    methods :{
        searchQuery(){
            console.log('search ' )
        },
        clear(){
            console.log('clear' )
        },
        exportTemp(){
            console.log('export template' )
        },
    }

  }
  </script>