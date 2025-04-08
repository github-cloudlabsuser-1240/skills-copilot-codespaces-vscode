# Login to Azure (if not already logged in)
Connect-AzAccount

# Variables
$resourceGroupName = "example-resources"
$location = "East US"
$vmName = "ExampleVM"
$adminUsername = "azureuser"
$adminPassword = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force
$size = "Standard_DS1_v2"

# Create a resource group (if it doesn't already exist)
if (-not (Get-AzResourceGroup -Name $resourceGroupName -ErrorAction SilentlyContinue)) {
    New-AzResourceGroup -Name $resourceGroupName -Location $location
}

# Create a virtual network
$vnet = New-AzVirtualNetwork -ResourceGroupName $resourceGroupName -Location $location `
    -Name "ExampleVNet" -AddressPrefix "10.0.0.0/16"

# Create a subnet
$subnet = Add-AzVirtualNetworkSubnetConfig -Name "ExampleSubnet" -AddressPrefix "10.0.0.0/24" -VirtualNetwork $vnet
$vnet | Set-AzVirtualNetwork

# Create a public IP address
$publicIp = New-AzPublicIpAddress -ResourceGroupName $resourceGroupName -Location $location `
    -Name "ExamplePublicIP" -AllocationMethod Dynamic

# Create a network security group
$nsg = New-AzNetworkSecurityGroup -ResourceGroupName $resourceGroupName -Location $location `
    -Name "ExampleNSG"

# Create a network interface
$nic = New-AzNetworkInterface -ResourceGroupName $resourceGroupName -Location $location `
    -Name "ExampleNIC" -SubnetId $subnet.Id -PublicIpAddressId $publicIp.Id -NetworkSecurityGroupId $nsg.Id

# Create a virtual machine configuration
$vmConfig = New-AzVMConfig -VMName $vmName -VMSize $size |
    Set-AzVMOperatingSystem -Windows -ComputerName $vmName -Credential (New-Object PSCredential ($adminUsername, $adminPassword)) |
    Set-AzVMSourceImage -PublisherName "MicrosoftWindowsServer" -Offer "WindowsServer" -Skus "2019-Datacenter" -Version "latest" |
    Add-AzVMNetworkInterface -Id $nic.Id

# Create the virtual machine
New-AzVM -ResourceGroupName $resourceGroupName -Location $location -VM $vmConfig

Write-Host "Virtual machine '$vmName' has been deployed successfully."