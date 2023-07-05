
<style scoped>

.layout-main{  
  height: 100%;
}
.div-app-caption{
 width: 400px;
  height: 40px;
  background: #5b6270;
    /* border-radius: 3px;
    float: left;
    position: relative;
    top: 15px;
    left: 20px; */
}
.layout-logo{
    width: 180px;
    height: 50px;
    /* background: #5b6270; */
    border-radius: 3px;
    float: left;
    position: relative;
    top: 5px;
    left: 5px;
}
.img-logo{
  position: relative;
  top: 5px;
  left: 0px;
  width: 35px;
  height: 35px;
}
.label-logo{
  color:blue;
  position: relative;
  top: -5px;
  left: 5px;
  font-size:20px;
}
.layout-nav{
    width: 200px;
    margin: 0 auto;
    margin-right: 0px;
}
.layout-footer-center{
    text-align: center;
}

.layout {
  border: 1px solid #d7dde4;
  background: #ffce7b;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
  height: 98%;
}
.layout-top{  
  height: 100%;
  
}
.layout-header-bar {
  width: 100%;
  display: flex;
  align-self: left;
  align-items: center;
  background:  #2c3e50;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
  margin-left:1px;
  margin-right:1px;
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

.main_content{
  background:  #fffffb;
  height: 95%;
}
.span-controle {
  /* //绀蓝#494e8f */
  color: white;
  font-size: 20px;
}
.textarea-screen {
  width: 100%;
  height: 500px;
  background: black;
  color: white;
}
.row-operation {
  display: flex;
  justify-content: center;
  border-radius: 5px;
  background: #d3d7d4;
  padding: 5px;
}
.div-image {
  display: flex;
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
</style>
<template>
  <div class="layout">
    <Layout class="layout-main">
    <Header style="padding:0px">
        <Menu mode="horizontal" theme="light" active-name="1" style="width:100%;height:64px;">
            <div class="layout-logo"><img class="img-logo" src="../images/logo.png"/><label class="label-logo">自动标定系统</label></div>        
            <div class="layout-nav">                
                <MenuItem name="1">
                    <Icon size="20" type="ios-notifications" color="#33a3dc"></Icon>
                    消息
                </MenuItem>
                <MenuItem name="2">
                    <Icon  size="20" type="ios-person" color="#33a3dc"></Icon>
                    用户
                </MenuItem>
            </div>
        </Menu>
    </Header>
    <Layout class="layout-top">    
        <Content class="main_content">
          <keep-alive>
          <router-view/>
          </keep-alive>     
        </Content>
      </Layout>
    </Layout>
  </div>
</template>