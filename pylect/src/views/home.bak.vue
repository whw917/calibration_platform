
<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f6f5ec;
  position: relative;
  border-radius: 4px;
  /* overflow: hidden; */
}
.layout-header-bar {
  background: #fff;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
}
.layout-logo-left {
  width: 90%;
  height: 30px;
  background: #5b6270;
  border-radius: 3px;
  margin: 15px auto;
}
.menu-icon {
  transition: all 0.3s;
}
.rotate-icon {
  transform: rotate(-90deg);
}
.menu-item span {
  display: inline-block;
  overflow: hidden;
  width: 69px;
  text-overflow: ellipsis;
  white-space: nowrap;
  vertical-align: bottom;
  transition: width 0.2s ease 0.2s;
}
.menu-item i {
  transform: translateX(0px);
  transition: font-size 0.2s ease, transform 0.2s ease;
  vertical-align: middle;
  font-size: 16px;
}
.collapsed-menu span {
  width: 0px;
  transition: width 0.2s ease;
}
.collapsed-menu i {
  transform: translateX(5px);
  transition: font-size 0.2s ease 0.2s, transform 0.2s ease 0.2s;
  vertical-align: middle;
  font-size: 22px;
}
.span-controle {
  /* //绀蓝#494e8f */
  color: #494e8f;
  font-size: 20px;
}
.textarea-screen {
  width: 99%;
  height: 500px;
  background: black;
  color: white;
}
.row-operation {
  display: flex;
  justify-content: center;
  border-radius: 5px;
  background: #d9d6c3;
  margin: 1px;
}
.div-com{  
  display: flex;
  justify-content: center;
  border-radius: 5px;
  /* background: #d3d7d4; */
  padding: 5px;
  height: 50px;
  margin: 20px;
  color:blue;
}
.div-image {
  display: flex;
  flex-direction: column;
  justify-content: center;
  border-radius: 5px;
  background: #d3d7d4;
  padding: 5px;
}
.img-operation {
  cursor: pointer;
  width: 50px;
  height: 50px;
}
.textarea-python{
  margin-top:10px;
  width: 100%;
  height: 100px;
 
}
.div-scroll-back{
  background: white;
  height: 100%;
}
.div-row-info{
  height: 40px;
  background: #d3d7d4;
  display: flex;
  align-items: center;
}
.row{
  margin:1px
}
.div-left-item{
  height: 82px;
  background: #d9d6c3;
  display: flex;
  align-items: center;
}
.div-select-com{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
  padding: 5px;
}
</style>

</style>
<template>
  
    
  <div class="layout">
     <Row>
      <i-col span=12>
        <Row class="row-operation">
          <div class="div-left-item">
            <Checkbox v-model="checkAllChannels">所有通道</Checkbox>
          </div>
        </Row>
      </i-col>
      <i-col span=12>
        <Row class="row-operation">
        
          <div
            class="div-image"
            id="div_img_start"
           
          >
            <img class="img-operation" src="../images/start.png" />
            <label>自动采集</label>
          </div>
          <div
            class="div-image"
            id="div_img_next"
          >
            <img class="img-operation" src="../images/next.png"/>
            <label>单步</label>
          </div>
          <div
            class="div-image"
            id="div_img_stop"
          >
            <img class="img-operation" src="../images/stop.png"/>
            <label>停止</label>
          </div>
          </Row>
          </i-col>
      </Row>
      <Row>        
        <i-col span=12>
          <div class="div-scroll-back">
            <Scroll ref="left_scroll"  v-bind:height="500">
              <Table width="100%" border :columns="scalList" :data="scalData"></Table>
            </Scroll>
          </div>
        </i-col>      
        <i-col span=12>
          <div class="div-scroll-back">
            <textarea ref="main_console" id="main_console" class="textarea-screen" :style="{height: 500}" v-model="pythonMessage">               
            </textarea>
          </div>
        </i-col>
      </Row>
      <Row>
        <label style="color:blue;margin:10px">指令操作</label>
        <i-col span=4>
        </i-col>      
        <i-col span=4>
          <div
            class="div-select-com"
          >
           <span>请选择设备的串口</span>
            <Select v-model="comInstrumentName" style="width:200px">
                <Option v-for="item in serialList" :value="item.name" :key="item.name">{{ item.title }}</Option>
            </Select>
          </div>
        </i-col>
        <i-col span=8>
          <Row>
            <label style="width:150px">总线地址</label> <Input v-model="value" placeholder="总线地址" style="width: 300px" /> <Button>读取</Button><Button>写入</Button>
          </Row>
          <Row>
            <label style="width:150px">设备ID</label> <Input v-model="value" placeholder="设备ID" style="width: 300px" /><Button>读取</Button><Button>写入</Button>
          </Row>  
          <Row>
            <label style="width:150px">采样间隔</label> <Input v-model="value" placeholder="采样间隔" style="width: 300px" /><Button>读取</Button><Button>写入</Button>
          </Row>
        </i-col>
        <i-col span=4>
        </i-col>
        <i-col span=4>
        </i-col>
      </Row>
      <Row>
        <label style="color:blue;margin:10px">数据转发</label>
      </Row>
      
      <Row>
        <label style="width:150px">转发地址1</label> <Input v-model="value" placeholder="转发地址1" style="width: 500px" /> <Button>保存</Button>
      </Row>
      <Row>
        <label style="width:150px">转发地址2</label> <Input v-model="value" placeholder="转发地址2" style="width: 500px" /> <Button>保存</Button>
      </Row>

  </div>
</template>
<script>
    export default {
      data () {
          return {
            value:"",
              checkAllChannels: false,
              pythonMessage:"python message",
              comInstrumentName:"",
              serialList:[
                  {
                      name: 'COM10',
                      title: 'COM10'
                  },
                  {
                      name: 'COM11',
                      title: 'COM11'
                  }

              ],
              scalList: [                 
                  {
                    type: 'selection',
                    width: 60,
                    align: 'center',
                    fixed: "left",
                },
                {
                  title: "设备编号",
                  key: "id",
                  width: 100
                },
                {
                  title: "设备类型",
                  key: "sensorType",
                  width: 150,
                },
                {
                  title: "端口",
                  key: "comName",
                  width: 150,
                },
                {
                  title: "地址",
                  key: "busAddr",
                  width: 100,
                },
                {
                  title: "状态",
                  key: "status",
                  width: 75,
                }
              ],
              scalData: [
                {
                  id: "1",
                  sensorType: "倾角X",
                  comName: "COM10",
                  busAddr: "1",
                  status: "正常",
                },
                {
                  id: "2",
                  sensorType: "倾角X",
                  comName: "COM10",
                  busAddr: "2",
                  status: "正常",
                },
                {
                  id: "3",
                  sensorType: "倾角X",
                  comName: "COM10",
                  busAddr: "3",
                  status: "正常",
                },
              ],
          }
      },      
      mounted() {
        let local = this;
        /* let val = this.$root.windowState.winHeight */
        window.addEventListener('pythonEvent',function (e) {  
          console.log(e)    
            /* local.$Message.info( e.data.msg ); */
            local.pythonMessage += "\r\n"+ e.data.msg +"\r\n" + e.data.value
        },true);
      },
    }
</script>