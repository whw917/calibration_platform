<style scoped>

.main-page{
    width: 80%;
    margin: auto;
    
}
.name-bar{
    width: 300px;
    float:left;
}

.other-bar{
    width: 300px;
    float: left;
}

.point-bar{
    width: 90%;
    float: left;

    margin-top: 40px ;
}

.left-col{
    width:30%;
}

.right-col{
    offset: 1;
    width:30%;
}
.form-item-label {
    width: 30%; /* Adjust this value as needed */
}

.buttons{
    margin-top: 10px;
}



</style>

<template>
    <Form class="main-page">

        <Row> 
            <Col class="left-col">
                <FormItem class="form-item-label"  label="流程名称:" >
                    <Input class="name-bar" v-model="queryParam.name" placeholder="name" clearable />
                </FormItem>

                <FormItem class="form-item-label" label="流程类型:">
                    <Select v-model="queryParam.type" class="other-bar">
                        <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                    </Select>
                </FormItem>

                <FormItem class="form-item-label" label="驱动协议:">
                    <Select v-model="queryParam.type" class="other-bar">
                        <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                    </Select>
                </FormItem>

                <FormItem class="form-item-label" label="传感器协议:">
                    <Select v-model="queryParam.type" class="other-bar">
                        <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                    </Select>
                </FormItem>

                

            </Col>

            <Col  class="right-col"> 

                <FormItem class="form-item-label" label="设备名称:">
                    <Input class="other-bar" v-model="queryParam.name" placeholder="name" clearable />
                </FormItem>

                <FormItem class="form-item-label" label="设备协议:">
                    <Input class="other-bar" v-model="queryParam.name" placeholder="name" clearable />
                </FormItem>

                <FormItem class="form-item-label" label="运动时间(s):">
                    <Input class="other-bar" v-model="queryParam.name" placeholder="name" clearable />
                </FormItem>

                <FormItem class="form-item-label" label="读数延时(s):">
                    <Input class="other-bar" v-model="queryParam.name" placeholder="name" clearable />
                </FormItem>
            </Col> 

            <Col class="right-col">
                <FormItem class="form-item-label" label="读数次数(次):">
                    <Input class="other-bar" v-model="queryParam.name" placeholder="name" clearable />
                </FormItem>

                <FormItem class="form-item-label" label="平台精度:">
                    <Input class="other-bar" v-model="queryParam.name" placeholder="name" clearable />
                </FormItem>

                <FormItem class="form-item-label" label="传感器轴数:">
                    <Select v-model="queryParam.type" class="other-bar">
                        <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                    </Select>
                </FormItem>

                <FormItem class="form-item-label" label="传感器名称:">
                    <Select v-model="queryParam.type" class="other-bar">
                        <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                    </Select>
                </FormItem>
            
            </Col>

        </Row>
                <FormItem label="点数列表:"  class="point-bar">
                    <Input v-model="queryParam.name" placeholder="name" size="large" clearable />

                    <Row class="buttons">
                    
                        <Col align="right">
                            <Button type="primary" @click="searchQuery" icon="search">确定</Button>
                            <Button type="primary">取消</Button>
                        </Col>
    
                    </Row>
                </FormItem>

                
                

         
    </Form>
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
            queryParam: {
                name: '',
                
            },
        }
        },
        methods: {

        }

  }
  </script>