from django.shortcuts import render, redirect
from .models import Experience , Doctor , Client , Booking
from .form import DoctorForm,ClientForm,ExperienceForm ,BookingForm
# Create your views here.
def index(request):
    # Doctor.Objects.get(id = 1).experience_set.all()
    x = {
        'doctors' : Doctor.objects.all(),
    }
    return render(request , 'index.html' , x)

def SignUpAsDoctor(request):
    if request.method == 'POST':
        newDoctoe = DoctorForm(request.POST , request.FILES)
        if newDoctoe.is_valid():
            newDoctoe.save()
            return redirect('/')
    data = {
        'Form' : DoctorForm(),
    }

    return render(request , 'signup.html',data)


def SignUpAsClient(request):
    if request.method == 'POST':
        newClient = ClientForm(request.POST)
        if newClient.is_valid():
            newClient.save()
            return redirect('/')
    data = {
        'Form': ClientForm(),
    }
    return render(request , 'signup.html' , data)

def login(request):
    if request.method == 'POST':
      username = request.POST['mail']
      password = request.POST['password']
      if request.POST['type'] == 'Doctor':
          type = Doctor
      else:
          type = Client
      try:
        login = type.objects.get(mail = username)
        if login.mail == username and login.password == password:
            if request.POST['type'] == 'Doctor':
                return redirect('doctorDetails/' + str(login.id))
            else:
                return redirect('book/' + str(login.id))
        else:
            return redirect('login')
      except:
          return redirect('login')
    else:
        return render(request, 'login.html')



def doctorDetails(request , id):
    doctor = Doctor.objects.get(id = id)
    if request.method == 'POST':
        doctor_show = DoctorForm(request.POST , request.FILES , instance=doctor)
        if doctor_show.is_valid():
            doctor_show.save()
            return redirect('/')
    else:
        doctor_show = DoctorForm(instance=doctor)
    context = {
            'doctorsDetails' : doctor_show,
            'doc' : doctor,
        }
    return render(request , 'doctor_details.html' , context)




def delete(request , id):
    context = {
        'id' : id,
    }
    doctor = Doctor.objects.get(id = id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('/')
    return render(request , 'delete.html' , context)



def addnewExperience(request ,id):
    doctor = Doctor.objects.get(id = id)
    form = ExperienceForm()
    if request.method == 'POST':
        form = ExperienceForm(request.POST or None)
        if form.is_valid():
            nameOfHospital = form.cleaned_data.get('name_of_hospital')
            yearOfExperience = form.cleaned_data.get('year_of_experience')
            experience = Experience(name_of_hospital = nameOfHospital , year_of_experience = yearOfExperience , Doctor = doctor)
            experience.save()
            return redirect('/doctorDetails/' + str(doctor.id))
    context = {
        'form' :form,
        'doc' : doctor,
    }
    return render(request , 'add_experience.html' , context)

def book(request , id):
    client = Client.objects.get(id = id)
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST or None)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            time = form.cleaned_data.get('time')
            doctor = form.cleaned_data.get('Doctor')
            print(date)
            print(time)
            book = Booking(name = client.name , mail = client.mail ,date = date , time = time,Doctor = doctor)
            book.save()
            return redirect('/')
    context = {
        'form' : form,
        'cli' : client,
    }
    return render(request , 'book.html' , context)
