#non-linear regression
one1(1:110)=1;
one2(1:40)=1;

[a1,a2,a3,a4,y1]=textread("Iris_data_norm_train.txt","%f,%f,%f,%f,%f");
[b1,b2,b3,b4,y2]=textread("iris_data_norm_test.txt","%f,%f,%f,%f,%f");

x1=[one1',a1,a2,a3,a4,a1.^2,a2.^2,a3.^2,a4.^2,a1.*a2,a1.*a3,a1.*a4,a2.*a3,a2.*a4,a3.*a4]; #contain train data
x2=[one2',b1,b2,b3,b4,b1.^2,b2.^2,b3.^2,b4.^2,b1.*b2,b1.*b3,b1.*b4,b2.*b3,b2.*b4,b3.*b4]; #contain test data

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

