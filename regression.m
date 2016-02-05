#linear regression

[a1,a2,a3,a4,y1]=textread("Iris_data_norm_train.txt","%f,%f,%f,%f,%f");
[b1,b2,b3,b4,y2]=textread("iris_data_norm_test.txt","%f,%f,%f,%f,%f");

x1=[a1,a2,a3,a4]; #contain train data
x2=[b1,b2,b3,b4]; #contain test data

w=inv(x1'*x1)*x1'*y1; #weight vector from train data

h=sign(x2*w);

N=length(y2);
count=0;

for i=1:N

	if h(i)!= y2(i)  #calculating misclassification point 
	count++;
	end
end

weight_vector=w

