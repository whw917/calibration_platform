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
        <h2 class="title">数据查询</h2>

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
                    <Button type="primary" @click="createNew" icon="search">新建</Button>
                    <Button type="primary" @click="importTemp" icon="search">导入</Button>
                    <Button type="primary" @click="downloadTemp" icon="search">下载模版</Button>
                </Col>

            </Row>

            <div class="table-page">
                <ProcessTable/>
            </div>   

        </Form>
  
    </div>
  </template>
  
  <script>
  import { Input, Button, Table, Page, Space, model, FormItem} from 'view-design'
  import ProcessTable from './processTable.vue'

  export default {
    components: {
      Input,
      Button,
      Table,
      Page,
      FormItem,

      ProcessTable,

    },
    data() {
        return {
            isCollapse: false,
            queryParam: {
                dateRecord: '',
                taskRecord: '',
                valueRecord: '',
            },
        }
    },
    methods :{
        searchQuery(){
            console.log('search ' )
        },
        createNew(){
            console.log('creat new' )
        },
        importTemp(){
            console.log('import template' )
        },
        downloadTemp(){
            console.log('download template' )
        },
    }

  }
  </script>